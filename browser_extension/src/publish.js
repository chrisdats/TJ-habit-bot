function publish() {
   
    pubnub = new PubNub({
        publishKey : 'pub-c-9008e2a2-1e7e-40a6-aa4e-a9f6ddffb04d',
        subscribeKey : 'sub-c-c00d7a36-13bb-11e8-a8e8-9e7f09a8f511'
    })

    function publishSampleMessage() {
        var publishConfig = {
            channel : "tab_activity",
            message : "TEST MESSAGE"
        }
        pubnub.publish(publishConfig, function(status, response) {
            console.log(status, response);
        })
    }
    
    pubnub.addListener({
        status: function(statusEvent) {
            if (statusEvent.category === "PNConnectedCategory") {
                publishSampleMessage();
            }
        },
        message: function(message) {
            console.log("NEW MESSAGE", message);
        },
        presence: function(presenceEvent) {
            // handle presence
        }
    })      
    console.log("Subscribing..");
    pubnub.subscribe({
        channels: ['tab_activity'] 
    });
  };


  