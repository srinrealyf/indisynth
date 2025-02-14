![alt text](./Assets/IndiSynth.png)

# IndiSynth

IndiSynth is a comprehensive synthetic data generator, designed to generate random and realistic (fake) data for 80+ Indian entities across multiple domains. It supports the generation of synthetic data for personal identity, business and tax-related data, banking, healthcare, and more.

## Installation

To install **IndiSynth**, use the following pip command:

```bash
pip install IndiSynth
```

## What is it?

IndiSynth is a specialized tool to generate synthetic Indian data, meeting the needs of Indian demographics in various sectors, including finance, healthcare, and commerce. It offers a wide range of localized data types, such as Aadhaar numbers, PAN cards, Indian phone numbers, postal codes, GSTINs, regional names, and more, thus providing realistic and culturally relevant datasets for testing and development. With accuracy and variety at its center, IndiSynth makes the process of generating high-quality, domain-specific synthetic data for use cases in India much easier.

## Supported Categories and Functions

### 1. PersonalIdentitySynth (Personal Identity)

| Function | Description |
|----------|-------------|
| `generate_aadhaar()` | Generates a random 12-digit Aadhaar number |
| `generate_pan()` | Generates a random PAN card number in the format `AAAAA1234A` |
| `generate_voter_id()` | Generates a random Voter ID |
| `generate_passport()` | Generates a random passport number |
| `generate_driving_license()` | Generates a random driving license number |
| `generate_birth_certificate()` | Generates a random birth certificate number |
| `generate_ration_card()` | Generates a random Ration Card number |

### 2. ContactAddressSynth (Contact & Address)

| Function | Description |
|----------|-------------|
| `generate_mobile_number()` | Generates a random 10-digit mobile number |
| `generate_landline_number()` | Generates a random landline number |
| `generate_pin_code()` | Generates a random 6-digit pin code |
| `generate_village_name()` | Generates a random village name |
| `generate_district_name()` | Generates a random district name |
| `generate_state_name()` | Generates a random state name |
| `generate_email_address()` | Generates a random email address |
| `generate_street_address()` | Generates a random street address with door number |

### 3. BusinessTaxSynth (Business & Tax)

| Function | Description |
|----------|-------------|
| `generate_gst_number()` | Generates a random GST number |
| `generate_cin()` | Generates a random CIN number |
| `generate_msme_udyam()` | Generates a random MSME/Udyam Registration number |
| `generate_tan()` | Generates a random TAN number |
| `generate_professional_tax_number()` | Generates a random professional tax number |
| `generate_shop_establishment_license()` | Generates a random shop and establishment license number |
| `generate_iec()` | Generates a random Import Export Code |
| `generate_fssai_license()` | Generates a random FSSAI license number |

### 4. BankingFinanceSynth (Banking & Finance)

| Function | Description |
|----------|-------------|
| `generate_bank_account_number()` | Generates a random 15-digit bank account number |
| `generate_ifsc_code()` | Generates a random IFSC code |
| `generate_micr_code()` | Generates a random MICR code |
| `generate_upi_id()` | Generates a random UPI ID |
| `generate_credit_card_number()` | Generates a random credit card number |
| `generate_debit_card_number()` | Generates a random debit card number |
| `generate_lic_policy_number()` | Generates a random LIC policy number |
| `generate_mutual_fund_folio_number()` | Generates a random mutual fund folio number |
| `generate_demat_account_number()` | Generates a random demat account number |

### 5. EducationSynth (Education)

| Function | Description |
|----------|-------------|
| `generate_student_id()` | Generates a random student ID number |
| `generate_board_roll_number()` | Generates a random board exam roll number |
| `generate_university_registration_number()` | Generates a random university registration number |
| `generate_udise_code()` | Generates a random school UDISE code |
| `generate_aishe_code()` | Generates a random AISHE code for a college |

### 6. EmploymentSynth (Employment)

| Function | Description |
|----------|-------------|
| `generate_epf_number()` | Generates a random EPF number |
| `generate_esi_number()` | Generates a random ESI number |
| `generate_uan()` | Generates a random UAN number |
| `generate_government_employee_id()` | Generates a random government employee ID |

### 7. VehicleSynth (Vehichle)

| Function | Description |
|----------|-------------|
| `generate_vehicle_registration_number()` | Generates a random vehicle registration number |
| `generate_rc_number()` | Generates a random RC number |
| `generate_chassis_number()` | Generates a random chassis number |
| `generate_engine_number()` | Generates a random engine number |
| `generate_driving_school_license()` | Generates a random driving school license number |

### 8. ProfessionalSynth (Professional)

| Function | Description |
|----------|-------------|
| `generate_medical_registration_number()` | Generates a random medical registration number |
| `generate_bar_council_registration()` | Generates a random bar council registration number |
| `generate_pharmacy_license_number()` | Generates a random pharmacy license number |
| `generate_ca_registration_number()` | Generates a random CA registration number |
| `generate_company_secretary_membership_number()` | Generates a random company secretary membership number |

### 9. PropertySynth (Property)

| Function | Description |
|----------|-------------|
| `generate_property_registration_number()` | Generates a random property registration number |
| `generate_khata_number()` | Generates a random Khata number |
| `generate_survey_number()` | Generates a random survey number |
| `generate_property_tax_assessment_number()` | Generates a random property tax assessment number |

### 10. UtilitiesSynth (Utilities)

| Function | Description |
|----------|-------------|
| `generate_electricity_consumer_number()` | Generates a random electricity consumer number |
| `generate_gas_connection_number()` | Generates a random gas connection number |
| `generate_water_connection_id()` | Generates a random water connection ID |
| `generate_broadband_customer_id()` | Generates a random broadband customer ID |
| `generate_dth_subscription_number()` | Generates a random DTH subscription number |

### 11. HealthcareSynth (Healthcare)

| Function | Description |
|----------|-------------|
| `generate_abha_number()` | Generates a random ABHA number |
| `generate_health_insurance_policy_number()` | Generates a random health insurance policy number |
| `generate_hospital_registration_number()` | Generates a random hospital registration number |
| `generate_medical_record_number()` | Generates a random medical record number |
| `generate_vaccine_certificate_number()` | Generates a random vaccine certificate number |

### 12. AgricultureSynth (Agriculture)

| Function | Description |
|----------|-------------|
| `generate_kisan_credit_card_number()` | Generates a random Kisan Credit Card number |
| `generate_farmer_registration_number()` | Generates a random farmer registration number |
| `generate_soil_health_card_number()` | Generates a random soil health card number |
| `generate_pm_kisan_beneficiary_id()` | Generates a random PM Kisan beneficiary ID |
| `generate_agriculture_land_registration()` | Generates a random agricultural land registration number |

### 13. GovernmentBenefitsSynth (Government Benefits)

| Function | Description |
|----------|-------------|
| `generate_bpl_card_number()` | Generates a random BPL card number |
| `generate_pension_payment_order()` | Generates a random pension payment order number |
| `generate_scholarship_id()` | Generates a random scholarship ID |
| `generate_social_security_number()` | Generates a random social security number |

### 14. LegalDocumentationSynth (Legal & Documentation)

| Function | Description |
|----------|-------------|
| `generate_court_case_number()` | Generates a random court case number |
| `generate_fir_number()` | Generates a random FIR number |
| `generate_advocate_registration()` | Generates a random advocate registration number |
| `generate_notary_license_number()` | Generates a random notary license number |

### 15. BusinessOperationsSynth (Business Operations)

| Function | Description |
|----------|-------------|
| `generate_factory_license_number()` | Generates a random factory license number |
| `generate_trademark_registration()` | Generates a random trademark registration number |
| `generate_patent_number()` | Generates a random patent number |
| `generate_copyright_registration()` | Generates a random copyright registration number |

### 16. TravelTourismSynth (Travel & Tourism)

| Function | Description |
|----------|-------------|
| `generate_air_india_frequent_flyer_number()` | Generates a random Air India frequent flyer number |
| `generate_railway_pnr()` | Generates a random railway PNR number |
| `generate_tourist_guide_license()` | Generates a random tourist guide license number |
| `generate_hotel_registration_number()` | Generates a random hotel registration number |

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👨🏻‍💻 Developed by Sai Raam at StatBir

For any queries, suggestions, or contributions, feel free to [reach out](https://www.linkedin.com/in/srinrealyf). Let's build and improve IndiSynth together!
