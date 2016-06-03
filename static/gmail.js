//Code taken from team Green Apples
//All credit to Winton Yee, Masahero Masuda, Ri Jiu Zheng, Jerry Lei
//https://github.com/jerrylei98/Teacher-Contact-Site


// Your Client ID can be retrieved from your project in the Google
// Developer Console, https://console.developers.google.com

var CLIENT_ID;

function initClientId(client_id){
    CLIENT_ID = client_id;
};

var SCOPES = ['profile', 'email'];

/**
 * Check if current user has authorized this application.
 */
function checkAuth() {
    gapi.auth.authorize(
        {
            'client_id': CLIENT_ID,
            'scope': SCOPES.join(' '),
            'immediate': true
        }, handleAuthResult);
};

/**
 * Handle response from authorization server.
 *
 * @param {Object} authResult Authorization result.
 */
function handleAuthResult(authResult) {
    if (authResult && !authResult.error) {
	    gapi.client.load('plus', 'v1').then(function() {
		var request = gapi.client.plus.people.get({
		    'userId': 'me'
		})
		request.then(function(resp) {
		    if(resp.result.domain === "stuy.edu"){
			$.getJSON("/addUser", {
			    'username': resp.result.displayName,
			    'email': resp.result.emails[0].value,
			    'auth': auth,
			}, function(data){
			    console.log(data);
			    window.location.reload(true)
//			    $('body').html(data);
			});
		    }else{
			signOut();
		    }
		}, function(reason) {
			console.log('Error: ' + reason.result.error.message);
		});
	    });
    }
}

/**
 * Initiate auth flow in response to user clicking authorize button.
 *
 * @param {Event} event Button click event.
 */
function handleAuthClick(event) {
    auth = event.target.id
    gapi.auth.authorize(
        {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
        handleAuthResult);
    return false;
};

/**
 * Sign a user out
 */
function signOut(){
    var winning = window.open("","","width=500,height=500");
    winning.location = "https://accounts.google.com/logout";
    setInterval(function(){
      try{
        winning.location.href;
      }
      catch(err){
        winning.close();
        window.location = "/logout";
      }
    }, 100);
}

document.getElementById('teacher').addEventListener("click", handleAuthClick);
document.getElementById('student').addEventListener("click", handleAuthClick);
