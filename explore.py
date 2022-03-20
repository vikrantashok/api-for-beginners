from twilio.rest import Client

client = Client(
    "AC4632cc5e2357d86872260437293cedc7",
    "05bbaf030e511b3079de745f764a22fa"
)

for msg in client.message.list():
    print(msg.body)


for msg in client.message.list():
    print(f"Deleting {msg.body}")
    msg.delete()

msg = client.message.create(
        to="+150314615537",
        from_="+12015848089",
        body="Hello from Python",
)


print(f"Created a new message: {msg.sid}")