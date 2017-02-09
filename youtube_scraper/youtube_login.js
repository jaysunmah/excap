var casper = require('casper').create();
var fs = require("fs");
var logName = 'output.txt';
var currentLinks = "";

casper.start('https://accounts.google.com/ServiceLogin?uilel=3&service=youtube&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Ffeature%3Dsign_in_button%26next%3D%252F%26hl%3Den%26action_handle_signin%3Dtrue%26app%3Ddesktop', function() {
    this.echo(this.getTitle());
	this.capture("a.png");
});

casper.then(function() {
	this.sendKeys('input#Email', 'kristinyin@gmail.com');
	this.click('input#next');
});

casper.wait(500, function() {
	this.echo("Input Username");
});

casper.then(function() {
	this.sendKeys('input#Passwd', 'icecream');
	this.click('input#signIn');
});


function getImages() {
	var scripts = document.querySelectorAll('img[src]');
    return Array.prototype.map.call(scripts, function (e) {
        return e.getAttribute('src');
    });
}

var imagesArray = [];

casper.waitForSelector('#yt-masthead', function() {
	imagesArray = this.evaluate(getImages);
	var self = this;
	imagesArray.forEach(function (item) {
		if (self.resourceExists(item)) {
			//self.echo(item + ' loaded');
			currentLinks += item + "\n"
		} else {
			var message = item + ' not loaded';
			self.echo(message, 'ERROR');
		}
	});
	fs.write(logName, currentLinks, 'w');
	this.echo("done");
});


casper.run();
