var tab = chrome.tabs;
console.log(tab);
var windows = chrome.windows;
console.log(windows);


chrome.runtime.onMessage.addListener(
    function(request){

        console.log(request.text);


		var xhr = new XMLHttpRequest();
				xhr.open("GET", "http://localhost:3000/", true);
				xhr.send();
				console.log("clicked");

//=============================================================================

		chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs){  
		    console.log(tabs[0].url);
		    if (tab.incognito == true	) {
				console.log("in incognito");
			} else {
				console.log("not in incognito");
			}
		});
       
});


 // chrome.tabs.query({active: true, lastFocusedWindow:true}, function(tabs){  
	// 	    console.log(tabs[0].url);
	// 	    if (windows.incognito) {
	// 			console.log("in incognito");
	// 		} else {
	// 			console.log("not in incognito");
	// 		}
	// });













// incognitoTab(tab);

// function incognitoTab (tab) {
// 	if (tab.incognito) {
// 		console.log("in incognito");
// 	} else {
// 		console.log("not in incognito");
// 	}
// }