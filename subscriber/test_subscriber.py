from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.pubnub import PubNub, SubscribeListener

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-c00d7a36-13bb-11e8-a8e8-9e7f09a8f511"
pnconfig.publish_key = "pub-c-9008e2a2-1e7e-40a6-aa4e-a9f6ddffb04d"
pnconfig.ssl = True

pubnub = PubNub(pnconfig)

my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels('tab_activity').execute()
my_listener.wait_for_connect()

print('connected')

while True:
    result = my_listener.wait_for_message_on('tab_activity')
    print(result.message)
