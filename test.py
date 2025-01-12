from indisynth.personal_identity import PersonalIdentitySynth
aadhaar = PersonalIdentitySynth.generate_aadhaar()
pan_card = PersonalIdentitySynth.generate_pan()
voter_id = PersonalIdentitySynth.generate_voter_id()
passport = PersonalIdentitySynth.generate_passport_number()
driving_license = PersonalIdentitySynth.generate_driving_license()

from indisynth.contact_address import ContactAddressSynth
address = ContactAddressSynth.generate_address()

from indisynth.business_tax import BusinessTaxSynth
tan = BusinessTaxSynth.generate_tan()

from indisynth.banking_finance import BankingFinanceSynth
acc_no = BankingFinanceSynth.generate_bank_account_number()
ifsc = BankingFinanceSynth.generate_ifsc_code()
micr = BankingFinanceSynth.generate_micr_code()
upi = BankingFinanceSynth.generate_upi_id()
credit_card = BankingFinanceSynth.generate_credit_card_number()
debit_card = BankingFinanceSynth.generate_debit_card_number()
lic_policy = BankingFinanceSynth.generate_lic_policy_number()
mutual_fund = BankingFinanceSynth.generate_mutual_fund_folio_number()
demat = BankingFinanceSynth.generate_demat_account_number()
expiry_date = BankingFinanceSynth.generate_card_expiry_date()


# print(expiry_date)


from indisynth.education import EducationSynth
roll_no = EducationSynth.generate_student_id()


from indisynth.employment import EmploymentSynth
pf_no = EmploymentSynth.generate_epf_number()

from indisynth.vehicle import VehicleSynth
reg_no = VehicleSynth.generate_vehicle_registration_number()

print(reg_no)