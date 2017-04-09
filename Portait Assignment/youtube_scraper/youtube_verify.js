var casper = require("casper").create({
  stepTimeout: 60000,
  timeout: 240000,
  verbose: true,
  onError: function(self, m) {
    console.log('FATAL:' + m);
    self.exit();
  },
});

var fs = require("fs");
var fileName = "canary.txt";
var successStatus = "failed";

casper.start('https://accounts.google.com/ServiceLogin?uilel=3&service=youtube&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Ffeature%3Dsign_in_button%26next%3D%252F%26hl%3Den%26action_handle_signin%3Dtrue%26app%3Ddesktop', function() {
    this.echo(this.getTitle());
});

casper.then(function() {
	fs.write(fileName, successStatus, 'w');
	this.echo("Inputting username...");
	this.sendKeys('input#Email', casper.cli.args[0]);
	this.click('input#next');
});

casper.wait(1000, function() {
	this.echo("Filling in password...");
});

casper.then(function() {
	this.sendKeys('input#Passwd', casper.cli.args[1]);
	this.click('input#signIn');
});

casper.waitForSelector('#yt-masthead', function() {
	this.echo("successful login!");
	successStatus = "success";
	fs.write(fileName, successStatus, 'w');
});

casper.run();
