import pdf2final_list
import text2ppt
import testPPTx

x=pdf2final_list.process(["Logistic Regression","python","Linear Regression"])
testPPTx.process_data_and_create_presentation(x)
