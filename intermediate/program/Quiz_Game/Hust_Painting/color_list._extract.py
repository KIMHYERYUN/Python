###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
# 이미지에서 색 축출 - 512 * 512 당 0.6s
colors = colorgram.extract('image.jpg', 30)
print(colors)
#[<colorgram.py Color: Rgb(r=245, g=243, b=238), 64.68350168350169%>, <colorgram.py Color: Rgb(r=246, g=242, b=244), 7.866161616161617%>, <colorgram.py Color: Rgb(r=202, g=164, b=110), 5.356902356902357%>, <colorgram.py Color: Rgb(r=240, g=245, b=241), 4.654882154882155%>, <colorgram.py Color: Rgb(r=236, g=239, b=243), 3.542929292929293%>, <colorgram.py Color: Rgb(r=149, g=75, b=50), 3.0555555555555554%>, <colorgram.py Color: Rgb(r=222, g=201, b=136), 1.5572390572390573%>, <colorgram.py Color: Rgb(r=53, g=93, b=123), 1.5454545454545454%>, <colorgram.py Color: Rgb(r=170, g=154, b=41), 1.4242424242424243%>, <colorgram.py Color: Rgb(r=138, g=31, b=20), 1.291245791245791%>, <colorgram.py Color: Rgb(r=134, g=163, b=184), 0.9646464646464646%>, <colorgram.py Color: Rgb(r=197, g=92, b=73), 0.6969696969696969%>, <colorgram.py Color: Rgb(r=47, g=121, b=86), 0.6346801346801347%>, <colorgram.py Color: Rgb(r=73, g=43, b=35), 0.43097643097643096%>, <colorgram.py Color: Rgb(r=145, g=178, b=149), 0.39478114478114473%>, <colorgram.py Color: Rgb(r=14, g=98, b=70), 0.3451178451178451%>, <colorgram.py Color: Rgb(r=232, g=176, b=165), 0.28787878787878785%>, <colorgram.py Color: Rgb(r=160, g=142, b=158), 0.26346801346801346%>, <colorgram.py Color: Rgb(r=54, g=45, b=50), 0.186026936026936%>, <colorgram.py Color: Rgb(r=101, g=75, b=77), 0.186026936026936%>, <colorgram.py Color: Rgb(r=183, g=205, b=171), 0.17255892255892255%>, <colorgram.py Color: Rgb(r=36, g=60, b=74), 0.14983164983164982%>, <colorgram.py Color: Rgb(r=19, g=86, b=89), 0.13215488215488214%>, <colorgram.py Color: Rgb(r=82, g=148, b=129), 0.06228956228956229%>, <colorgram.py Color: Rgb(r=147, g=17, b=19), 0.04461279461279461%>, <colorgram.py Color: Rgb(r=27, g=68, b=102), 0.02104377104377104%>, <colorgram.py Color: Rgb(r=12, g=70, b=64), 0.019360269360269362%>, <colorgram.py Color: Rgb(r=107, g=127, b=153), 0.013468013468013467%>, <colorgram.py Color: Rgb(r=176, g=192, b=208), 0.0101010101010101%>, <colorgram.py Color: Rgb(r=168, g=99, b=102), 0.005892255892255892%>]

for color in colors:
    #위 리스트에서 rgb 칼라만 추출가능
    #rgb_colors.append(color.rgb)
#print(rgb_colors)
# [Rgb(r=245, g=243, b=238), Rgb(r=246, g=242, b=244), Rgb(r=202, g=164, b=110), Rgb(r=240, g=245, b=241), Rgb(r=236, g=239, b=243), Rgb(r=149, g=75, b=50), Rgb(r=222, g=201, b=136), Rgb(r=53, g=93, b=123), Rgb(r=170, g=154, b=41), Rgb(r=138, g=31, b=20), Rgb(r=134, g=163, b=184), Rgb(r=197, g=92, b=73), Rgb(r=47, g=121, b=86), Rgb(r=73, g=43, b=35), Rgb(r=145, g=178, b=149), Rgb(r=14, g=98, b=70), Rgb(r=232, g=176, b=165), Rgb(r=160, g=142, b=158), Rgb(r=54, g=45, b=50), Rgb(r=101, g=75, b=77), Rgb(r=183, g=205, b=171), Rgb(r=36, g=60, b=74), Rgb(r=19, g=86, b=89), Rgb(r=82, g=148, b=129), Rgb(r=147, g=17, b=19), Rgb(r=27, g=68, b=102), Rgb(r=12, g=70, b=64), Rgb(r=107, g=127, b=153), Rgb(r=176, g=192, b=208), Rgb(r=168, g=99, b=102)]
    #각 색깔 추출하는 함수 - r,g,b
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
#[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
