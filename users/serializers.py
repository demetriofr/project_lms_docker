from rest_framework import serializers


from .models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(source='payment_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        """
        Custom logic for converting a model object into a dictionary for serialization.
        """

        ret = super().to_representation(instance)

        # Проверяем, является ли текущий пользователь владельцем объекта
        is_owner = self.context['request'].user == instance

        # Если текущий пользователь не владелец объекта и не является администратором
        if not is_owner and not self.context['request'].user.is_staff:
            for field in ['password', 'last_name', 'payment_set']:
                ret.pop(field, None)

        return ret
