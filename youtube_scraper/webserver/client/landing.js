Template.landing.events({
  'click #runScript' (event) {

    var username = $('#username').val();
    var password = $('#password').val();

    var cb = function(error, response) {
      if (response) {
        var saveImagesCb = function(error, response) {
          if (response) {
            var parseImagesCb = function(error, response) {
              if (response) {
                var arrangeFilesCb = function(error, response) {
                  Session.set("loadingData", false);
                  Router.go("/view_image/" + username);
                }
                $('#loadingInfo').progress({ percent: 100 });
                Session.set("loadingStatus", "100% Prepping files...");
                Meteor.call("arrangeFiles", username, password, arrangeFilesCb);
              }
            }
            $('#loadingInfo').progress({ percent: 60 });
            Session.set("loadingStatus", "70% Processing data...");
            Meteor.call("parseImages", username, password, parseImagesCb);
          }
        }
        $('#loadingInfo').progress({ percent: 45 });
        Session.set("loadingStatus", "45% Saving images...");
        Meteor.call("saveImages", username, password, saveImagesCb);
      }
    }
    Meteor.call("youtubeLogin", $('#username').val(), $('#password').val(), cb);
    Session.set("loadingData", true)

    Meteor.setTimeout(function() {
      Session.set("loadingStatus", "30% Scraping Youtube images...")
      $('#loadingInfo').progress({ percent: 30 });
    }, 50);

  },
});

Template.landing.helpers({
  loadingData: function() {
    return Session.get("loadingData");
  },
  loadingStatus: function() {
    return Session.get("loadingStatus");
  },
});

Template.landing.onRendered(function() {
  if (Session.get('renderedLanding')) {
    $('#landingContainer').transition({
  		animation: 'fade right',
  		duration: transitionDelay,
  	});
  } else {
    Session.set('renderedLanding', true);
  	$('#landingContainer').transition({
  		animation: 'fade left',
  		duration: transitionDelay,
  	});
  }
});
