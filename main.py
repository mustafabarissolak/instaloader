import instaloader
import bilgiler

L = instaloader.Instaloader()

username = bilgiler.username
password = bilgiler.password
L.login(username, password)

profile = instaloader.Profile.from_username(L.context, username)

# takipçileri al
print("Takipçiler yazılıyor...")

for followers in profile.get_followers():
    with open("takipci.txt", "a+") as f:
        file = f.write(followers.username + '\n')

# takip edilenleri al
print("Takip edilenler yazılıyor...")

for followees in profile.get_followees():
    with open("takipedilen.txt", "a+") as f:
        file = f.write(followees.username + '\n')

#takip etmeyenleri bul

followers_file = set(open("takipci.txt").readlines())
followees_file = set(open("takipedilen.txt").readlines())
unfollowers_set = followees_file.difference(followers_file)

# Geri tapiip etmeyenleri al
print("Geri takip yapmayanlar yaziliyor...")
sayac = 1
for i in unfollowers_set:
    with open("gt_yapmayanlar.txt", "a+") as f:
        file = f.write(f"{sayac}: {i}")
    sayac += 1

print("İşlem bitti..")
