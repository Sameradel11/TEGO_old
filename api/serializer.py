from rest_framework import serializers
from .models import CustomUser, Company, Owner


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'email', 'mobile_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        exclude = ['company']


class CompanySerializer(serializers.ModelSerializer):
    owners = OwnerSerializer(many=True,)
    # stakeholders_set=StakeholdersSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        owners=validated_data.pop('owners')
        company=Company.objects.create(**validated_data)
        print(company)
        for owner in owners:
            Owner.objects.create(**owner,company=company)
        return company

    def update(self,instace,validated_data):
        owners=validated_data.pop('owners')
        company=Company.objects.create(**validated_data)
        instace.name=validated_data.get('name',instace.name)
        instace.location=validated_data.get('location',instace.name)
        instace.commercial_registration_number=validated_data.get(
            'commercial_registration_number',
            instace.commercial_registration_number)
        instace.tax_card_number=validated_data.get('tax_card_number',
        instace.tax_card_number)
        instace.mobile=validated_data.get('mobile',instace.mobile)
        instace.landline=validated_data.get('landline',instace.landline)
        instace.fax_number=validated_data.get('fax_number',instace.fax_number)
        instace.company_type=validated_data.get('company_type',instace.company_type)
        instace.company_capital=validated_data.get('company_capital',instace.company_capital)

        instace.save()
        return instace




