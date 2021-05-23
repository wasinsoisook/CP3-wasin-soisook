from tkinter import *
import math

def bmi_calculate(event):
    num_result = round(float(textbox_weight.get()) / math.pow(float(textbox_height.get()) / 100,2), 1)
    matrix = ""
    if num_result >= 30:
        matrix = "อ้วนมาก (30.0 ขึ้นไป)ค่อนข้างอันตราย เพราะเข้าเกณฑ์อ้วนมาก " \
                 "\nเสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน หากค่า BMI อยู่ในระดับนี้ " \
                 "จะต้องระวังการรับประทานไขมัน \nและควรออกกำลังกายอย่างสม่ำเสมอ และหากเลขยิ่งสูงกว่า 40.0 " \
                 "ยิ่งแสดงถึงความอ้วนที่มากขึ้น "
    elif num_result >= 25.0 and num_result <= 29.9:
        matrix = "น้ำหนักเกิน (23.0 - 24.9)พยายามอีกนิดเพื่อลดน้ำหนักให้เข้าสู่ค่ามาตรฐาน \nเพราะค่า BMI " \
                 "ในช่วงนี้ยังถือว่าเป็นกลุ่มผู้ที่มีความอ้วนอยู่บ้าง แม้จะไม่ถือว่าอ้วน " \
                 "\nแต่หากประวัติคนในครอบครัวเคยเป็นโรคเบาหวานและความดันโลหิตสูง ก็ถือว่ายังมีความเสี่ยงมากกว่าคนปกติ "
    elif num_result >= 18.6 and num_result <= 22.9:
        matrix = "น้ำหนักปกติ เหมาะสม (18.6 - 22.9)น้ำหนักที่เหมาะสมสำหรับคนไทยคือค่า BMI ระหว่าง 18.5-22.9 " \
                 "\nจัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่าง ๆ \nน้อยที่สุด " \
                 "ควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับนี้ให้นานที่สุด "
    elif num_result <= 18.5:
        matrix = "ผอมเกินไป (น้อยกว่า 18.5)น้ำหนักน้อยกว่าปกติก็ไม่ค่อยดี หากคุณสูงมากแต่น้ำหนักน้อยเกินไป " \
                 "\nอาจเสี่ยงต่อการได้รับสารอาหารไม่เพียงพอหรือได้รับพลังงานไม่เพียงพอ ส่งผลให้ร่างกายอ่อนเพลียง่าย " \
                 "\nการรับประทานอาหารให้เพียงพอและออกกำลังกายแบบเวทเทรนนิ่งเพื่อเสริมสร้างกล้ามเนื้อ " \
                 "\nสามารถช่วยเพิ่มค่า BMI ให้อยู่ในเกณฑ์ปกติได้ "
    result.configure(text= str(num_result) + "\n" + matrix)

main = Tk()
Height = Label(main, text="ส่วนสูง(cm)").grid(row=0, column=0)
textbox_height = Entry(main)
textbox_height.grid(row=0, column=1)
Weight = Label(main, text="น้ำหนัก(Kg)").grid(row=1, column=0)
textbox_weight = Entry(main)
textbox_weight.grid(row=1, column=1)
calculate = Button(main, text = "คำนวณ")
calculate.bind('<Button-1>', bmi_calculate)
calculate.grid(row=2,column=0)
result = Label(main, text= "Result")
result.grid(row=2,column=1)
main.mainloop()
