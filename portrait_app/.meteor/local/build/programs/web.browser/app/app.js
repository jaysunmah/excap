var require = meteorInstall({"client":{"main.html":["./template.main.js",function(require,exports,module){

///////////////////////////////////////////////////////////////////////
//                                                                   //
// client/main.html                                                  //
//                                                                   //
///////////////////////////////////////////////////////////////////////
                                                                     //
module.exports = require("./template.main.js");                      // 1
                                                                     // 2
///////////////////////////////////////////////////////////////////////

}],"template.main.js":function(){

///////////////////////////////////////////////////////////////////////
//                                                                   //
// client/template.main.js                                           //
//                                                                   //
///////////////////////////////////////////////////////////////////////
                                                                     //
                                                                     // 1
Template.body.addContent((function() {                               // 2
  var view = this;                                                   // 3
  return [ HTML.Raw("<h1>Welcome to Meteor!</h1>\n\n  "), Spacebars.include(view.lookupTemplate("hello")), "\n  ", Spacebars.include(view.lookupTemplate("info")) ];
}));                                                                 // 5
Meteor.startup(Template.body.renderToDocument);                      // 6
                                                                     // 7
Template.__checkName("hello");                                       // 8
Template["hello"] = new Template("Template.hello", (function() {     // 9
  var view = this;                                                   // 10
  return [ HTML.Raw("<button>Click Me</button>\n  "), HTML.P("You've pressed the button ", Blaze.View("lookup:counter", function() {
    return Spacebars.mustache(view.lookup("counter"));               // 12
  }), " times.") ];                                                  // 13
}));                                                                 // 14
                                                                     // 15
Template.__checkName("info");                                        // 16
Template["info"] = new Template("Template.info", (function() {       // 17
  var view = this;                                                   // 18
  return HTML.Raw('<h2>Learn Meteor!</h2>\n  <ul>\n    <li><a href="https://www.meteor.com/try" target="_blank">Do the Tutorial</a></li>\n    <li><a href="http://guide.meteor.com" target="_blank">Follow the Guide</a></li>\n    <li><a href="https://docs.meteor.com" target="_blank">Read the Docs</a></li>\n    <li><a href="https://forums.meteor.com" target="_blank">Discussions</a></li>\n  </ul>');
}));                                                                 // 20
                                                                     // 21
///////////////////////////////////////////////////////////////////////

},"main.js":["meteor/templating","meteor/reactive-var","./main.html",function(require,exports,module){

///////////////////////////////////////////////////////////////////////
//                                                                   //
// client/main.js                                                    //
//                                                                   //
///////////////////////////////////////////////////////////////////////
                                                                     //
var Template;module.import('meteor/templating',{"Template":function(v){Template=v}});var ReactiveVar;module.import('meteor/reactive-var',{"ReactiveVar":function(v){ReactiveVar=v}});module.import('./main.html');
                                                                     // 2
                                                                     //
                                                                     // 4
                                                                     //
Template.hello.onCreated(function () {                               // 6
  function helloOnCreated() {                                        // 6
    // counter starts at 0                                           // 7
    this.counter = new ReactiveVar(0);                               // 8
  }                                                                  // 9
                                                                     //
  return helloOnCreated;                                             // 6
}());                                                                // 6
                                                                     //
Template.hello.helpers({                                             // 11
  counter: function () {                                             // 12
    function counter() {                                             // 11
      return Template.instance().counter.get();                      // 13
    }                                                                // 14
                                                                     //
    return counter;                                                  // 11
  }()                                                                // 11
});                                                                  // 11
                                                                     //
Template.hello.events({                                              // 17
  'click button': function () {                                      // 18
    function clickButton(event, instance) {                          // 17
      // increment the counter when button is clicked                // 19
      instance.counter.set(instance.counter.get() + 1);              // 20
    }                                                                // 21
                                                                     //
    return clickButton;                                              // 17
  }()                                                                // 17
});                                                                  // 17
///////////////////////////////////////////////////////////////////////

}]}},{"extensions":[".js",".json",".html",".css"]});
require("./client/template.main.js");
require("./client/main.js");