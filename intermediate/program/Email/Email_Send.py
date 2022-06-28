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

