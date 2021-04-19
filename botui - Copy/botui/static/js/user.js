/////This the backend logic for the user page
document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    //var socket = io.connect('http://' + document.domain + ':' + location.port);
    // var socket = io.connect('https://ant--bot.herokuapp.com');
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    //var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var bot_switch = 1;

    // Connect to server
    socket.on('connect', data => {
        console.log(3);

    })

    //intro messages
    var botui = new BotUI('delivery-bot');

    answers = ["Antopolis is an innovation driven enterprise that provides a range of tech and marketing services tailored to EMPOWER CHANGEMAKERS.",
        "House 87-89, Road 4, Block B, Niketan 1212 Dhaka, Dhaka Division, Bangladesh", "PLease Fill The Form Below and click on the red button to submit"
    ]
    Tech = "1.Mobile App Services &nbsp&nbsp  2.Web Services";
    DM = "1.Content Management &nbsp&nbsp  2.Social Media Management &nbsp&nbsp  3.Customer care  &nbsp&nbsp 4.Digital Campaigns";
    MP = "2D Animation  ,&nbsp&nbsp 3D Animation  &nbsp&nbsp ,Motion Pictures";
    ///Introductory Message
    botui.message.bot({
        delay: 1000,
        loading: true,
        content: "Hello I am Rayhanur.How may I help you"
    })

    ///introductory buttons
    function intro() {
        botui.action.button({
            loading: true,
            delay: 1000,
            action: [{ // show only one button
                text: 'Who are you',
                value: 1
            }, { // show only one button
                text: 'Where are you located',
                value: 2
            }, { // show only one button
                text: 'What are your services',
                value: 3
            }, { // show only one button
                text: 'Get a Quotation',
                value: 4
            }]
        }).then(function(res) { // will be called when a button is clicked.

            if (res.value < 3) {
                botui.message.bot({
                    delay: 1000,
                    loading: true,
                    content: answers[(res.value) - 1]
                })
                botui.action.button({
                    delay: 1000,
                    loading: true,
                    action: [{
                        text: "Want to know more?",
                        value: 1
                    }]
                }).then(function(res) {
                    if (res.value == 1) {
                        intro();
                    }
                })
            }
            if (res.value == 3) {
                botui.message.bot({
                    delay: 1000,
                    loading: true,
                    content: 'What would you like to know about'

                })
                botui.action.button({
                    delay: 1000,
                    loading: true,
                    action: [{ // show only one button
                            text: 'Tech',
                            value: Tech
                        }, { // show only one button
                            text: 'Digital Marketing',
                            value: DM
                        }, { // show only one button
                            text: 'Motion Pictures',
                            value: MP
                        }

                    ]
                }).then((function(res) { // will be called when a button is clicked.

                    botui.message.bot({
                        delay: 1000,
                        loading: true,
                        content: res.value
                    })
                    botui.action.button({
                        delay: 2000,
                        loading: true,
                        action: [{
                            text: "Want to know more?",
                            value: 1
                        }]
                    }).then(function(res) {
                        if (res.value == 1) {
                            intro();
                        }
                    })


                }))
            }
            if (res.value == 4) {
                botui.action.text({
                    action: [{
                        placeholder: "Enter Your name",
                    }]
                }).then(function(res) {
                    if (res.value == 1) {
                        console.log(res.value)
                    }
                    if (res.value == 2) {
                        console.log(res.value)
                    }
                    if (res.value == 3) {
                        console.log(res.value)
                    }
                    if (res.value == 4) {
                        console.log(res.value)
                    }
                    if (res.value == 5) {
                        console.log(res.value)
                    }
                })

            }


        });

    }
    intro();
    ///Socket receiving reply from agent side
    socket.on('user', function in_(data) {

            var botHtml = data;
            console.log(data)
            botui.message.bot({
                delay: 1000,
                loading: true,
                content: botHtml
            })



        })
        //socket receiving reply from Bot
    socket.on('bot', function in_(data) {

            var botHtml = data;
            console.log(data)
            botui.message.bot({
                delay: 1000,
                loading: true,
                content: botHtml
            })
            if (data == "Please wait a customer care agent will contact you") {
                //turn off bot
                bot_switch = 0;
                //then send message to agent event
                socket.emit('agent', {
                    data: "A User needs your help",
                    id: 1
                })

            }


        })
        //events after pressing enter
    $("#text").keypress(function(e) {

        var botHtml
        if (e.which == 13) {
            str = $("#text").val();

            botui.action.hide();
            console.log(botHtml);
            $("#text").val(" ");
            botui.message.human({
                    content: str
                })
                //if bot is on then send data to bot else to the agent
            if (bot_switch == 1) {
                socket.emit('bot', str);
            } else {
                socket.emit('agent', {
                    data: str,
                    id: 1
                })
            }



            //     // socket.once('bot', function in_(data) {

            //     //     var botHtml = data;
            //     //     console.log(data)
            //     //     botui.message.bot({
            //     //         delay: 1000,
            //     //         loading: true,
            //     //         content: botHtml
            //     //     })


            // })




        }
    })




});



//