var PubNub = require('pubnub');

pubnub = new PubNub({
    publishKey : 'pub-c-9008e2a2-1e7e-40a6-aa4e-a9f6ddffb04d',
    subscribeKey : 'sub-c-c00d7a36-13bb-11e8-a8e8-9e7f09a8f511',
    ssl: true
});

pubnub.subscribe({
    channels: ['tab_activity']
});

pubnub.addListener({message: function(m) {
    console.log(m.message);
}});


