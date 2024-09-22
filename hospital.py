from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox


class Hospital:
   
   
   
   def __init__(self,root): #construction , self and root is the window name
        # self: Refers to the current instance of the class. It allows access to the attributes and methods of the class.
        # root: This is the window object (passed to the class when it is created) that represents the main Tkinter window.

        self.root = root #self.root: The label is created inside the root window.
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")#window size
        
        self.NameOftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nshNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        #top title
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times ner roman",40,"bold"))
        lbltitle.pack(side=TOP,fill=X)
# pack() is a geometry manager in Tkinter that controls where and how the widget is placed in the window.
# side=TOP: Places the label at the top of the window.
# fill=X: Makes the label stretch horizontally across the width of the window.
        # =============DATA Frame============
        Dataframe = Frame(self.root,bd = 20, relief=RIDGE)
        Dataframe.place(x=0,y=90,width=1280,height=500)

        DataframeLeft = LabelFrame(Dataframe,bd= 10,relief=RIDGE,padx=10,
                                        font=("times ner roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=0,width=850,height=450)

        DataframeRight=LabelFrame(Dataframe,bd= 10,relief=RIDGE,padx=10,
                                        font=("times ner roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=860,y=0,width=390,height=350)

        # ================= Buttons Frame=====================
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=450,width=1280,height=70)

        # ================= Details Frame=====================

        Detailsframe = Frame(self.root,bd = 20, relief=RIDGE)
        Detailsframe.place(x=0,y=500,width=1280,height=190)

        # ====================Dataframe Left==============================
        
        lblNameTablet = Label(DataframeLeft,text="Name of the Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet = ttk.Combobox(DataframeLeft,font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        textref = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        textref.grid(row=1,column=1)

        lblDose = Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2)
        lblDose.grid(row=2,column=0,sticky=W)
        textDose = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        textDose.grid(row=2,column=1)

        lblNoOftablets = Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=4)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        textNoOftablets = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NumberOfTablets,width=35)
        textNoOftablets.grid(row=3,column=1)

        lblLot = Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        textLot = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        textLot.grid(row=4,column=1)

        lblissueDate = Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        textissueDate = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.IssueDate,width=35)
        textissueDate.grid(row=5,column=1)

        lblExpDate = Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        textExpDate = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        textExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        textDailyDose = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        textDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        textSideEffect = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=35)
        textSideEffect.grid(row=8,column=1)

        lblFurtherinfo = Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        textFurtherinfo = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        textFurtherinfo.grid(row=0,column=3)

        lblBloodPressure = Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        textBloodPressure = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        textBloodPressure.grid(row=1,column=3)

        lblStorage = Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        textStorage = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        textStorage.grid(row=2,column=3)

        lblMedicine = Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        textMedicine = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        textMedicine.grid(row=3,column=3)

        lblPatientId = Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        textPatientId = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        textPatientId.grid(row=4,column=3)

        lblNhsNumber = Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        textNhsNumber = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nshNumber,width=35)
        textNhsNumber.grid(row=5,column=3)

        lblPatientName = Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        textPatientName = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        textPatientName.grid(row=6,column=3)

        lblDateOfBirth = Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        textDateOfBirth = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        textDateOfBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        textPatientAddress = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        textPatientAddress.grid(row=8,column=3)

        # ===========================DataFrame Right================================================

        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=35)
        self.txtPrescription.grid(row=0,column=0)

        # ================== Buttons=======================

        btnPrescription=Button(Buttonframe,text="Presciption",bg="green",fg="White",font=("arial",12,"bold"),width=20,height=1,padx=0,pady=0)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Presciption Data",bg="green",fg="White",font=("arial",12,"bold"),width=20,height=1,padx=0,pady=0)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="White",font=("arial",12,"bold"),width=20,height=1,padx=0,pady=0)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="White",font=("arial",12,"bold"),width=20,height=1,padx=0,pady=0)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="White",font=("arial",12,"bold"),width=20,height=1,padx=0,pady=0)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="White",font=("arial",12,"bold"),width=20,height=1,padx=0,pady=0)
        btnExit.grid(row=0,column=5)

        # ================Table=====================
        # =====================Scrollbar======================

        scroll_x=ttk.Scrollbar(Dataframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dataframe,orient=HORIZONTAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftables","ref","dose","nooftables","lot","issuedate",
                        "expdate","dailydose","storage","nshnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftables",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftables",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nshnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftables",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftables",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nshnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=70)
        self.hospital_table.column("address",width=100)

        self.hospital_table.grid(row=2,column=0,sticky="nsew")

# ======================function declaration==============================
        def isPrescriptionDate(self):
            if self.Nameoftablets.get()=="" or self.ref.get()=="":
               Message.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Aratisahu@668",database="hospital")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.NumberOfTablets.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.IssueDate.get(),
                                                                                                        self.ExpDate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.sideEffect.get(),
                                                                                                        self.FurtherInformation.get(),
                                                                                                        self.StorageAdvice.get(),
                                                                                                        self.DrivingUsingMachine.get(),
                                                                                                        self.HowToUseMedication.get(),
                                                                                                        self.PatientId.get(),
                                                                                                        self.nshNumber.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.DateOfBirth.get(),
                                                                                                        self.PatientAddress.get()
                                                                                                        ))
                conn.commit()
                conn.close()

        root = Tk()#object of class
        ob = Hospital(root)
        root.mainloop()#close main loop