# GYAITR
## نظام ذكاء اصطناعي للتعامل مع الصور والفيديوهات، كتغيير الألوان وإضافة المؤثرات وتغيير الحجم إلخ...

<p align="center"><img src="https://github.com/tlersa/GYAITR/assets/111729973/92096dbc-62b5-4b82-b865-2d5bae306204" alt="شعار GYAITR" width="650"></p>


### الأوامر بسيطة جدا وكل شيء واضح، الأوامر الأساسية :
- الخيار 1 قراءة أبعاد الصور والبكسل.
- الخيار 2 فتح الصور والفيديوهات من الجهاز وفتح الكاميرا.
- الخيار 3 تغيير حجم الصور والفيديوهات، وتتوفر للصور 5 أوضاع وللفيديوهات وضعين فقط.
- الخيار 4 تعديل الصور والفيديوهات كالتالي :
  - تغيير الألوان كالتالي : 
    - RGB → Gray
    - RGB → HSV
    - RGB → LAB
    - RGB → XYZ
    - RGB → YCrCb
    - LAB → RGB
    - XYZ → RGB
    - YCrCb → RGB
  - إضافة الثأثيرات (للصور فقط)
    - Blur
    - Edge Cascade
    - Dilated
    - Eroded
    - 
### المميزات
- مجاني ومفتوح المصدر ✔️
- إذا لم تكن مثبت المكاتب المطلوبة cv2, os, timer سيتم تثبيتها تلقائيا ✔️
- حفظ الصور والفيديوهات بعد تعديلها، وبصيغة (png, jpg, mp4)، وتحديد مكان حفظها ✔️
- تحديد درجة التأثيرات والأشياء الإضافية كما تريد لراحة المستخدم ✔️
- عند حدوث خطأ من المستخدم ككتابة مسار الصورة الخاطئ مثلا سيتم إخباره بنص واضح لحل المشكلة ✔️
  
### ملاحظات ⚠️
- عندما تفتح صورة بواسطة النظام وتريد إغلاقها تستطيع ضغط أي زر بلوحة المفاتيح لإغلاقها، وللفيديوهات اضغط زر Q.
- عند إغلاق الفيديوهات يمكن أن تعلّق واجهة مفسر لغة Python التي تعرض الفيديو ببعض الأجهزة، وهذا شيء طبيعي لا تقلق منه.

### تثبيت المكاتب
```
pip install opencv-python os time
```

### [نسخة .exe للـWindows](https://t.me/tler_sa/156)
