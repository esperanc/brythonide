//
// Wrap the local module variables 
//
var codeSetup = (function() {


    // These will hold handles to asynchronous code that processing or other
    // libraries set up. We need them to cancel these callbacks after
    // the script is interrupted
    var intervalFuncVars = [];
    var timeoutFuncVars = [];
    var eventListeners = [];
    var requestId;


    // Must capture the setInterval function so that processing errors
    // are caught and sent to the output and so we know which asynchronous
    // processes were started
    var oldSetInterval = window.setInterval;
    var oldSetTimeout = window.setTimeout;
    var oldAddEventListener = window.addEventListener;
    var oldRequestAnimationFrame = window.requestAnimationFrame;

    // The window stop function if browser supports it
    //var windowStop = window.stop || function () {};

    // To be called before running a script that will be later stopped
    function runCode () {

        // Overwrite setInterval so we can log the timers
        window.setInterval = function (f,t) {
            var handle = 
            oldSetInterval (function () {
                try {
                    f()
                } catch (err) {
                    // Report error 
                    restoreAsync();
                    console.log ("setInterval error:"+ err.toString());
                    throw (err);
                }
            },t);
            intervalFuncVars.push(handle);
            return handle;
        }

        // Overwrite setTimeout so we can log the timers
        window.setTimeout = function (f,t) {
            var handle = 
            oldSetTimeout (function () {
                try {
                    f();
                } catch (err) {
                    // Report error and abort
                    restoreAsync();
                    console.log ("setTimeout error:"+ err.toString());
                    throw(err);
                }
            },t);
            timeoutFuncVars.push(handle);
            return handle;
        }


        window.addEventListener = function () {
            eventListeners.push (arguments);
            return oldAddEventListener.apply (this, arguments);
        }


        window.requestAnimationFrame = function () {
            requestId = oldRequestAnimationFrame.apply (this, arguments);
            return requestId;
        }
    }


    function stopCode ( status ) {

        // Cancel callbacks 

        for (var i = 0; i < intervalFuncVars.length; i++) {
            window.clearInterval (intervalFuncVars[i]);
        }
        intervalFuncVars = [];
        for (var i = 0; i < timeoutFuncVars.length; i++) {
            window.clearTimeout (timeoutFuncVars[i]);
        }
        timeoutFuncVars = [];
        for (var i = 0; i < eventListeners.length; i++) {
            window.removeEventListener.apply(null,eventListeners[i]);
        }
        if (requestId) {
            window.cancelAnimationFrame(requestId);
        }
        requestId = undefined;

        // Restore original timer environment 
        window.setInterval = oldSetInterval;
        window.setTimeout = oldSetTimeout;
        window.addEventListener = oldAddEventListener;

        window.addEventListener('error', function (e) {e.preventDefault();e.stopPropagation();}, false);

        var handlers = [
            'copy', 'cut', 'paste',
            'beforeunload', 'blur', 'change', 'click', 'contextmenu', 'dblclick', 'focus', 'keydown', 'keypress', 'keyup', 'mousedown', 'mousemove', 'mouseout', 'mouseover', 'mouseup', 'resize', 'scroll',
            'DOMNodeInserted', 'DOMNodeRemoved', 'DOMNodeRemovedFromDocument', 'DOMNodeInsertedIntoDocument', 'DOMAttrModified', 'DOMCharacterDataModified', 'DOMElementNameChanged', 'DOMAttributeNameChanged', 'DOMActivate', 'DOMFocusIn', 'DOMFocusOut', 'online', 'offline', 'textInput',
            'abort', 'close', 'dragdrop', 'load', 'paint', 'reset', 'select', 'submit', 'unload'
        ];

        function stopPropagation (e) {
            e.stopPropagation();
            // e.preventDefault(); // Stop for the form controls, etc., too?
        }
        for (var i=0; i < handlers.length; i++) {
            window.addEventListener(handlers[i], function (e) {stopPropagation(e);}, true);
        }
      
    }

    // Exported functions
    return {
        stop : stopCode,
        run : runCode,
    }
})();

codeSetup.run();


