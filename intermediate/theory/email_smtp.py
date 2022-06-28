"""
smtplib : 이메일 전송 모듈
Email SMTP : 이메일을 인터넷의 어떤 주소로도 발송할 수 있게 해줌
Simple Mail Transfer Protocol
sender - sender mail server - receiver mail server - receiver

1. 이메일 서비스 제공 업체의 smtp 주소가 맞는지 확인
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com

2. 보안 수준이 낮은 앱의 액세스’를 허용했는지 확인
3. Gmail 캡차(CAPTCHA)를 통과
4. smtplib.SMTP("smtp.gmail.com", port=587)
"""
import smtplib

my_email = "90x619@gmail.com"
password = ""
#방법1
#연결
connection = smtplib.SMTP("smtp.gmail.com")
#TLS(Transport Layer Security) : 이메일 서버와의 연결을 안전하게 만드는 방식
connection.starttls()
#로그인
connection.login(user=my_email, password=password)
#메일보내기
connection.sendmail(from_addr=my_email,
                    to_addrs="jaydenkhr@gmail.com",
                    msg="Subject:Hello\n\nThis is test")
#닫기
connection.close()


#방법2
with smtplib.SMTP("smtp.gmail.com") as connection:
    # TLS(Transport Layer Security) : 이메일 서버와의 연결을 안전하게 만드는 방식
    connection.starttls()
    # 로그인
    connection.login(user=my_email, password=password)
    # 메일보내기
    connection.sendmail(from_addr=my_email,
                        to_addrs="jaydenkhr@gmail.com",
                        msg="Subject:Hello\n\nThis is test")
    # 닫기
    connection.close()