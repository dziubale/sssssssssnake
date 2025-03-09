import pygame
import time
import random

pygame.init()

# رنگ
سیاہ = (0, 0, 0)
سفید = (255, 255, 255)
سرخ = (213, 50, 80)
سبز = (0, 255, 0)
نیلا = (50, 153, 213)

# ونڈو کی سائز
چوڑائی = 600
اونچائی = 400

ونڈو = pygame.display.set_mode((چوڑائی, اونچائی))
pygame.display.set_caption('سانپ کا کھیل')

# وقت
گھنٹہ = pygame.time.Clock()

# سانپ کی خصوصیات
سانپ_چوڑائی = 10
سانپ_اونچائی = 10
سانپ_کی_رفتار = 15

فونٹ_اسٹائل = pygame.font.SysFont("bahnschrift", 25)
اسکور_فونٹ = pygame.font.SysFont("comicsansms", 35)

def تمہاری_اسکور(اسکور):
    value = اسکور_فونٹ.render("اسکور: " + str(اسکور), True, سفید)
    ونڈو.blit(value, [0, 0])

def ہمارا_سانپ(سانپ_چوڑائی, سانپ_اونچائی, سانپ_لسٹ):
    for حصہ in سانپ_لسٹ:
        pygame.draw.rect(ونڈو, سبز, [حصہ[0], حصہ[1], سانپ_چوڑائی, سانپ_اونچائی])

def پیغام(msg, رنگ):
    mesg = فونٹ_اسٹائل.render(msg, True, رنگ)
    ونڈو.blit(mesg, [چوڑائی / 6, اونچائی / 3])

def کھیل():
    کھیلنا = True
    ختم = False

    x1 = چوڑائی / 2
    y1 = اونچائی / 2

    x1_تبدیلی = 0
    y1_تبدیلی = 0

    سانپ_لسٹ = []
    سانپ_کی_لمبائی = 1

    کھانا_x = round(random.randrange(0, چوڑائی - سانپ_چوڑائی) / 10.0) * 10.0
    کھانا_y = round(random.randrange(0, اونچائی - سانپ_اونچائی) / 10.0) * 10.0

    while کھیلنا:

        while ختم:
            ونڈو.fill(نیلا)
            پیغام("آپ ہار گئے! کھیل ختم کرنے کے لیے Q دبائیں یا دوبارہ کوشش کرنے کے لیے C دبائیں", سرخ)
            تمہاری_اسکور(سانپ_کی_لمبائی - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        کھیلنا = False
                        ختم = False
                    if event.key == pygame.K_c:
                        کھیل()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                کھیلنا = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_تبدیلی = -سانپ_چوڑائی
                    y1_تبدیلی = 0
                elif event.key == pygame.K_RIGHT:
                    x1_تبدیلی = سانپ_چوڑائی
                    y1_تبدیلی = 0
                elif event.key == pygame.K_UP:
                    y1_تبدیلی = -سانپ_اونچائی
                    x1_تبدیلی = 0
                elif event.key == pygame.K_DOWN:
                    y1_تبدیلی = سانپ_اونچائی
                    x1_تبدیلی = 0

        if x1 >= چوڑائی or x1 < 0 or y1 >= اونچائی or y1 < 0:
            ختم = True
        x1 += x1_تبدیلی
        y1 += y1_تبدیلی
        ونڈو.fill(نیلا)
        pygame.draw.rect(ونڈو, سرخ, [کھانا_x, کھانا_y, سانپ_چوڑائی, سانپ_اونچائی])
        سانپ_سر = []
        سانپ_سر.append(x1)
        سانپ_سر.append(y1)
        سانپ_لسٹ.append(سانپ_سر)
        if len(سانپ_لسٹ) > سانپ_کی_لمبائی:
            del سانپ_لسٹ[0]

        for حصہ in سانپ_لسٹ[:-1]:
            if حصہ == سانپ_سر:
                ختم = True

        ہمارا_سانپ(سانپ_چوڑائی, سانپ_اونچائی, سانپ_لسٹ)
        تمہاری_اسکور(سانپ_کی_لمبائی - 1)

        pygame.display.update()

        if x1 == کھانا_x and y1 == کھانا_y:
            کھانا_x = round(random.randrange(0, چوڑائی - سانپ_چوڑائی) / 10.0) * 10.0
            کھانا_y = round(random.randrange(0, اونچائی - سانپ_اونچائی) / 10.0) * 10.0
            سانپ_کی_لمبائی += 1

        گھنٹہ.tick(سانپ_کی_رفتار)

    pygame.quit()
    quit()

کھیل()
