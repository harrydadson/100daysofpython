class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print('Im a Teacher')

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    # Encapsulation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def update_memb(self, new_memb):
        self.membership_type = new_memb

    def read_cust():
        return 'reading customers'

    def __str__(self):
        print('converting to string')
        return self.name + " " + self.membership_type

    def print_all_cust(customers):
        for customer in customers:
            print(customer)

c = Customer('Harry', 'Gold')
print(c.name, c.membership_type)

customers = [Customer('Harry', 'Gold'), Customer('Maddy', 'Platinum')]
print(customers[1].name)

customers[1].update_memb('Diamond')
print(customers[1].membership_type) # or

customers[0].membership_type = 'Silver'
print(customers[0].membership_type)

print(Customer.read_cust())

print(customers[1])

Customer.print_all_cust(customers)


import re

words = re.findall('[A-z]\w+', press_release)
print(words)
   
output = {}

# populate dict
#loop through all words
for word in words:
    #check if doesnt  already exists in dict
    if word[0].lower() not in output.keys():
        output[word[0].lower()] = set()
        
    output[word[0].lower()].add(word)
    
print(output)

SELECT ss.SAP_SALES_ORD_NUM, ss.SAAS_SRC_CODE, ss.BILL_TO_CUST_NUM, ss.CNTRY_CODE, ss.CREATE_DATE, ss.CUM_CVRAGE_TERM, ss.CURRNCY_CODE, ss.CVRAGE_TERM,
		ss.END_DATE, ss.IBM_CNTRY_CODE, ss.IBM_CNTRY_CODE_BILL_TO, ss.IBM_CNTRY_CODE_RSEL, ss.IBM_END_USER_CUST_NUM, ss.IBM_SOLD_TO_CUST_NUM,
		ss.LINE_ITEM_SEQ_NUM, ss.LINE_ITEM_ID, ss.OPPRTNTY_NUM, ss.PART_NUM, ss.PART_QTY, ss.PROVISND_DATE, ss.RSEL_CUST_NUM, ss.SAAS_ANL_CMMTMT_VAL,
		ss.SAAS_TOT_CMMTMT_VAL, ss.SALES_ORD_DATE, ss.SAP_BILLG_FRQNCY_OPT_CODE,ss.SAP_DISTRIBTN_CHNL_CODE, ss.SIGNING_TYPE_CODE, ss.SIGNING_DATE,
		ss.ADD_DATE, ss.SRC_ADD_DATE, ss.START_DATE, ss.MOD_DATE, ss.RELEASE_DATE, ss.SOLD_TO_CUST_NUM, ss.SAP_SALES_ORG_CODE, ss.TCV_TYPE_IND , ss.SAAS_SRC_CODE
FROM saas2.saas_signings ss
WHERE SAP_SALES_ORD_NUM IN ('0077428598','0078428599')
AND SIGNING_TYPE_CODE LIKE '%NEW%'
AND LINE_ITEM_SEQ_NUM = '10'
WITH ur;