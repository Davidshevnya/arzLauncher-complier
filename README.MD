# Arizona Launcher Compiler
����� �������� �� ������, ������� ���������� ��� ���������� � ������� ���� ����� �� �������. ������ ����� �������� ������ � ������ �� ������� � ��������, ���� ������� �������� ����� ��������� � �������.

# ��������� � ������ ����������
## ��� 1. ���������� Python3
 �������� ��� ���� �� ���. [�����](https://python.org) ���� � [Microsoft Store](ms-windows-store://pdp?hl=uk-ua&gl=us&referrer=storeforweb&source=https%3A%2F%2Fapps.microsoft.com%2Fdetail%2F9ncvdn91xzqp%3Fhl%3Den-US%26gl%3DUS&productid=9ncvdn91xzqp&storecid=storeweb-pdp-open-cta&webid=f8e7e7bf-2ca3-489e-80aa-515bd872be7c&websessionid=7b73c923-0511-4cf6-aba6-b4fd22da6a44).
## ��� 2. �������� ������
��� ������ ����� ������� ������, ��� ����� ������� �� ���� [������](https://github.com/Davidshevnya/arzLauncher-complier/archive/refs/heads/main.zip).
�������������� ��� � ����� ��� ��� ������� �����, � ����� �������� ���.
## ��� 3. ����������� app.asar
����� ����� ��� ����� app.asar �� �������� ������� ��� �������� (�� ������ ������ �������� ������ ���), ������ ������� �� [�����](https://github.com/Davidshevnya/arzLauncher-complier/releases).
<br>������ ���� ����� ����������� � ����� � ������ main.py.
��� ��� ��� ������ ���������: ![alt text](readme/image-1.png)
## ��� 4. ��������� ������������ � ������ main.py
�������� ��������� ������ � ����� ������� � ��������� ��� ���������  �������: <br>
### ```pip install -r requirements.txt```<br>
### ```python main.py app.asar```

## ��� 5. �������� ��� �������� � ������� ������

���� � ��� app.asar �� �������� �������, �� ���������� 1 � ���� ������ 2. ���� ��� ���� ��� � ����������. 
### ����� ������ ����� ���������?
������ ��� app.asar.
<br> ��� ������� ������ �� app.asar`� �� �������.
������� ��������� �������� ������ � ������ ��������.
�� ������ ���� ����� ������, ��� ��������� ������ ������ ����� ������ ������ <br>https://api.ko-rista.com/v1/getLauncherImages?launcher_key=cfc629a1c42304558e2e9222c8bc0b26&type=background. <br>������� �� ������, �� ������� ������� ��� ������� ����������� ��������, ������ �� ����� �� ����� ������, ��� ����� ������ ������ �� ����� ������� �����������.
![alt text](readme/image-4.png) 
������� �������� ��� ���� �����. ![alt text](readme/image-5.png)
�� ������ ����� ������ ������� ����� ��������, � ������: <br>https://api.ko-rista.com/v1/getLauncherLink?launcher_key=cfc629a1c42304558e2e9222c8bc0b26&type=siteUrl <br> ������ �� ���������� ��������� type � ������, �� ����� ������, ��� ��� ������ ������ ����� �� ���� ������ �������. �� ������ �������� ������ ������� ����� �������������� ������ �� ��� ���� � ���������� ��� �� ����� ���-��������(������������� ��� ���, ��� ����� ������ ������ � �������� �����������, ����� �� ������������� ������� ��� ������ ����� ������), � ������ ������ ������� ������ ������.<br>
� ��� ����. ![alt text](readme/image-6.png) ��������� �� ������ � ����� ���������: ![alt text](readme/image-7.png) <br> ����� �� ������ ���������� ��� ��� ������ �������� � ��������. ������� ��� ���� ��� ��������: ����������� ������ � ������������. ��� ������������� ��� ����������� ��� �������. ���� �� ������ ������ ��� �����, � ������ ``query.php`` � ``server-data.php`` �������� [�����](https://github.com/Davidshevnya/arzLauncher-complier/tree/main/readme/dynamics_online).
����������� ������ ������ ����, ������ � ������ ������ �� �������. ����� ���� ��� ������, ������ �������� ``server-data.php`` �� ����� �����, ���������� ������ �� ���� � �������� � �����. <br> ��� �� ������, ���� ���� ��� ��������? <br> ��������� �� [pastebin](https://pastebin.com/) � ����������� ��������������, ����� � ������� ����� ���� ������ ���� � �������. ���� ������� ������ Paste � ������ ���� ���������:```{"arizona":[{"number":1,"name":"ArizonaRp","ip":"141.94.184.110","port":7777,"online":0,"maxplayers":150,"password":false}]}``` ������ ����![](readme/image-8.png)
������� ��� ���� � ��������� ����� ������ ������ ``Create New Paste``. ��� ������������ �� ���� �����, ������� �� ������ �������. ![alt text](readme/image-9.png) ��������� ������ ``raw`` � ��������� ������ ���� ��� ����������, ��������� �� � �����.


## ��� 6. �������� ������� � ���������� ��������������� app.asar
��������� �� [������](https://github.com/Davidshevnya/arzLauncher-complier/releases/download/launcher/Launcher.zip) � �������� ����� ��������, �������������� ��� � ����� ������� �����, � ����� �������� �����. �� ������� ����� ``resources`` � ��� �� ������ ���������� app.asar �� ����� ��������� output (������ ����).
![alt text](readme/image-2.png)��� ��� ������ �����:![alt text](readme/image-3.png)

## ��� 7. ��������� �������.