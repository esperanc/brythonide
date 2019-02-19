import sys
from browser import window

p5 = window.p5

def run():
    
    frame = sys._getframe(0)

    def sketch(p):
        #
        # Import p5 constants into top level name space
        # 
        frame.f_locals["P2D"] = p.P2D
        frame.f_locals["WEBGL"] = p.WEBGL
        frame.f_locals["ARROW"] = p.ARROW
        frame.f_locals["CROSS"] = p.CROSS
        frame.f_locals["HAND"] = p.HAND
        frame.f_locals["MOVE"] = p.MOVE
        frame.f_locals["TEXT"] = p.TEXT
        frame.f_locals["WAIT"] = p.WAIT
        frame.f_locals["HALF_PI"] = p.HALF_PI
        frame.f_locals["PI"] = p.PI
        frame.f_locals["QUARTER_PI"] = p.QUARTER_PI
        frame.f_locals["TAU"] = p.TAU
        frame.f_locals["TWO_PI"] = p.TWO_PI
        frame.f_locals["DEGREES"] = p.DEGREES
        frame.f_locals["RADIANS"] = p.RADIANS
        frame.f_locals["DEG_TO_RAD"] = p.DEG_TO_RAD
        frame.f_locals["RAD_TO_DEG"] = p.RAD_TO_DEG
        frame.f_locals["CORNER"] = p.CORNER
        frame.f_locals["CORNERS"] = p.CORNERS
        frame.f_locals["RADIUS"] = p.RADIUS
        frame.f_locals["RIGHT"] = p.RIGHT
        frame.f_locals["LEFT"] = p.LEFT
        frame.f_locals["CENTER"] = p.CENTER
        frame.f_locals["TOP"] = p.TOP
        frame.f_locals["BOTTOM"] = p.BOTTOM
        frame.f_locals["BASELINE"] = p.BASELINE
        frame.f_locals["POINTS"] = p.POINTS
        frame.f_locals["LINES"] = p.LINES
        frame.f_locals["LINE_STRIP"] = p.LINE_STRIP
        frame.f_locals["LINE_LOOP"] = p.LINE_LOOP
        frame.f_locals["TRIANGLES"] = p.TRIANGLES
        frame.f_locals["TRIANGLE_FAN"] = p.TRIANGLE_FAN
        frame.f_locals["TRIANGLE_STRIP"] = p.TRIANGLE_STRIP
        frame.f_locals["QUADS"] = p.QUADS
        frame.f_locals["QUAD_STRIP"] = p.QUAD_STRIP
        frame.f_locals["CLOSE"] = p.CLOSE
        frame.f_locals["OPEN"] = p.OPEN
        frame.f_locals["CHORD"] = p.CHORD
        frame.f_locals["PIE"] = p.PIE
        frame.f_locals["PROJECT"] = p.PROJECT
        frame.f_locals["SQUARE"] = p.SQUARE
        frame.f_locals["ROUND"] = p.ROUND
        frame.f_locals["BEVEL"] = p.BEVEL
        frame.f_locals["MITER"] = p.MITER
        frame.f_locals["RGB"] = p.RGB
        frame.f_locals["HSB"] = p.HSB
        frame.f_locals["HSL"] = p.HSL
        frame.f_locals["AUTO"] = p.AUTO
        frame.f_locals["ALT"] = p.ALT
        frame.f_locals["BACKSPACE"] = p.BACKSPACE
        frame.f_locals["CONTROL"] = p.CONTROL
        frame.f_locals["DELETE"] = p.DELETE
        frame.f_locals["DOWN_ARROW"] = p.DOWN_ARROW
        frame.f_locals["ENTER"] = p.ENTER
        frame.f_locals["ESCAPE"] = p.ESCAPE
        frame.f_locals["LEFT_ARROW"] = p.LEFT_ARROW
        frame.f_locals["OPTION"] = p.OPTION
        frame.f_locals["RETURN"] = p.RETURN
        frame.f_locals["RIGHT_ARROW"] = p.RIGHT_ARROW
        frame.f_locals["SHIFT"] = p.SHIFT
        frame.f_locals["TAB"] = p.TAB
        frame.f_locals["UP_ARROW"] = p.UP_ARROW
        frame.f_locals["BLEND"] = p.BLEND
        frame.f_locals["ADD"] = p.ADD
        frame.f_locals["DARKEST"] = p.DARKEST
        frame.f_locals["LIGHTEST"] = p.LIGHTEST
        frame.f_locals["DIFFERENCE"] = p.DIFFERENCE
        frame.f_locals["EXCLUSION"] = p.EXCLUSION
        frame.f_locals["MULTIPLY"] = p.MULTIPLY
        frame.f_locals["SCREEN"] = p.SCREEN
        frame.f_locals["REPLACE"] = p.REPLACE
        frame.f_locals["OVERLAY"] = p.OVERLAY
        frame.f_locals["HARD_LIGHT"] = p.HARD_LIGHT
        frame.f_locals["SOFT_LIGHT"] = p.SOFT_LIGHT
        frame.f_locals["DODGE"] = p.DODGE
        frame.f_locals["BURN"] = p.BURN
        frame.f_locals["THRESHOLD"] = p.THRESHOLD
        frame.f_locals["GRAY"] = p.GRAY
        frame.f_locals["OPAQUE"] = p.OPAQUE
        frame.f_locals["INVERT"] = p.INVERT
        frame.f_locals["POSTERIZE"] = p.POSTERIZE
        frame.f_locals["DILATE"] = p.DILATE
        frame.f_locals["ERODE"] = p.ERODE
        frame.f_locals["BLUR"] = p.BLUR
        frame.f_locals["NORMAL"] = p.NORMAL
        frame.f_locals["ITALIC"] = p.ITALIC
        frame.f_locals["BOLD"] = p.BOLD
        frame.f_locals["LINEAR"] = p.LINEAR
        frame.f_locals["QUADRATIC"] = p.QUADRATIC
        frame.f_locals["BEZIER"] = p.BEZIER
        frame.f_locals["CURVE"] = p.CURVE
        frame.f_locals["STROKE"] = p.STROKE
        frame.f_locals["FILL"] = p.FILL
        frame.f_locals["TEXTURE"] = p.TEXTURE
        frame.f_locals["IMMEDIATE"] = p.IMMEDIATE
        frame.f_locals["NEAREST"] = p.NEAREST
        frame.f_locals["REPEAT"] = p.REPEAT
        frame.f_locals["CLAMP"] = p.CLAMP
        frame.f_locals["MIRROR"] = p.MIRROR
        frame.f_locals["LANDSCAPE"] = p.LANDSCAPE
        frame.f_locals["PORTRAIT"] = p.PORTRAIT
        frame.f_locals["GRID"] = p.GRID
        frame.f_locals["AXES"] = p.AXES

        #
        # Import p5 variables and functions into top level name space
        # 
        frame.f_locals["remove"] = p.remove
        #frame.f_locals["canvas"] = p.canvas
        frame.f_locals["width"] = p.width
        frame.f_locals["height"] = p.height
        #frame.f_locals["drawingContext"] = p.drawingContext
        frame.f_locals["pmouseX"] = p.pmouseX
        frame.f_locals["pmouseY"] = p.pmouseY
        frame.f_locals["pwinMouseX"] = p.pwinMouseX
        frame.f_locals["pwinMouseY"] = p.pwinMouseY
        frame.f_locals["registerPreloadMethod"] = p.registerPreloadMethod
        frame.f_locals["registerMethod"] = p.registerMethod
        frame.f_locals["print"] = p.print
        frame.f_locals["frameCount"] = p.frameCount
        frame.f_locals["focused"] = p.focused
        frame.f_locals["cursor"] = p.cursor
        frame.f_locals["frameRate"] = p.frameRate
        frame.f_locals["getFrameRate"] = p.getFrameRate
        frame.f_locals["setFrameRate"] = p.setFrameRate
        frame.f_locals["noCursor"] = p.noCursor
        frame.f_locals["displayWidth"] = p.displayWidth
        frame.f_locals["displayHeight"] = p.displayHeight
        frame.f_locals["windowWidth"] = p.windowWidth
        frame.f_locals["windowHeight"] = p.windowHeight
        frame.f_locals["fullscreen"] = p.fullscreen
        frame.f_locals["pixelDensity"] = p.pixelDensity
        frame.f_locals["displayDensity"] = p.displayDensity
        frame.f_locals["getURL"] = p.getURL
        frame.f_locals["getURLPath"] = p.getURLPath
        frame.f_locals["getURLParams"] = p.getURLParams
        frame.f_locals["exit"] = p.exit
        frame.f_locals["pushStyle"] = p.pushStyle
        frame.f_locals["popStyle"] = p.popStyle
        frame.f_locals["size"] = p.size
        frame.f_locals["camera"] = p.camera
        frame.f_locals["perspective"] = p.perspective
        frame.f_locals["ortho"] = p.ortho
        frame.f_locals["createCamera"] = p.createCamera
        frame.f_locals["setCamera"] = p.setCamera
        frame.f_locals["setAttributes"] = p.setAttributes
        #frame.f_locals["createCanvas"] = p.createCanvas
        frame.f_locals["resizeCanvas"] = p.resizeCanvas
        frame.f_locals["noCanvas"] = p.noCanvas
        frame.f_locals["createGraphics"] = p.createGraphics
        frame.f_locals["blendMode"] = p.blendMode
        frame.f_locals["noLoop"] = p.noLoop
        frame.f_locals["loop"] = p.loop
        frame.f_locals["push"] = p.push
        frame.f_locals["pop"] = p.pop
        frame.f_locals["redraw"] = p.redraw
        frame.f_locals["applyMatrix"] = p.applyMatrix
        frame.f_locals["popMatrix"] = p.popMatrix
        frame.f_locals["printMatrix"] = p.printMatrix
        frame.f_locals["pushMatrix"] = p.pushMatrix
        frame.f_locals["resetMatrix"] = p.resetMatrix
        frame.f_locals["rotate"] = p.rotate
        frame.f_locals["rotateX"] = p.rotateX
        frame.f_locals["rotateY"] = p.rotateY
        frame.f_locals["rotateZ"] = p.rotateZ
        frame.f_locals["scale"] = p.scale
        frame.f_locals["shearX"] = p.shearX
        frame.f_locals["shearY"] = p.shearY
        frame.f_locals["translate"] = p.translate
        frame.f_locals["arc"] = p.arc
        frame.f_locals["ellipse"] = p.ellipse
        frame.f_locals["line"] = p.line
        frame.f_locals["point"] = p.point
        frame.f_locals["quad"] = p.quad
        frame.f_locals["rect"] = p.rect
        frame.f_locals["triangle"] = p.triangle
        frame.f_locals["ellipseMode"] = p.ellipseMode
        frame.f_locals["noSmooth"] = p.noSmooth
        frame.f_locals["rectMode"] = p.rectMode
        frame.f_locals["smooth"] = p.smooth
        frame.f_locals["strokeCap"] = p.strokeCap
        frame.f_locals["strokeJoin"] = p.strokeJoin
        frame.f_locals["strokeWeight"] = p.strokeWeight
        frame.f_locals["bezier"] = p.bezier
        frame.f_locals["bezierDetail"] = p.bezierDetail
        frame.f_locals["bezierPoint"] = p.bezierPoint
        frame.f_locals["bezierTangent"] = p.bezierTangent
        frame.f_locals["curve"] = p.curve
        frame.f_locals["curveDetail"] = p.curveDetail
        frame.f_locals["curveTightness"] = p.curveTightness
        frame.f_locals["curvePoint"] = p.curvePoint
        frame.f_locals["curveTangent"] = p.curveTangent
        frame.f_locals["beginContour"] = p.beginContour
        frame.f_locals["beginShape"] = p.beginShape
        frame.f_locals["bezierVertex"] = p.bezierVertex
        frame.f_locals["curveVertex"] = p.curveVertex
        frame.f_locals["endContour"] = p.endContour
        frame.f_locals["endShape"] = p.endShape
        frame.f_locals["quadraticVertex"] = p.quadraticVertex
        frame.f_locals["vertex"] = p.vertex
        frame.f_locals["alpha"] = p.alpha
        frame.f_locals["blue"] = p.blue
        frame.f_locals["brightness"] = p.brightness
        frame.f_locals["color"] = p.color
        frame.f_locals["green"] = p.green
        frame.f_locals["hue"] = p.hue
        frame.f_locals["lerpColor"] = p.lerpColor
        frame.f_locals["lightness"] = p.lightness
        frame.f_locals["red"] = p.red
        frame.f_locals["saturation"] = p.saturation
        frame.f_locals["background"] = p.background
        frame.f_locals["clear"] = p.clear
        frame.f_locals["colorMode"] = p.colorMode
        frame.f_locals["fill"] = p.fill
        frame.f_locals["noFill"] = p.noFill
        frame.f_locals["noStroke"] = p.noStroke
        frame.f_locals["stroke"] = p.stroke
        frame.f_locals["createStringDict"] = p.createStringDict
        frame.f_locals["createNumberDict"] = p.createNumberDict
        #frame.f_locals["deviceOrientation"] = p.deviceOrientation
        frame.f_locals["accelerationX"] = p.accelerationX
        frame.f_locals["accelerationY"] = p.accelerationY
        frame.f_locals["accelerationZ"] = p.accelerationZ
        frame.f_locals["pAccelerationX"] = p.pAccelerationX
        frame.f_locals["pAccelerationY"] = p.pAccelerationY
        frame.f_locals["pAccelerationZ"] = p.pAccelerationZ
        frame.f_locals["rotationX"] = p.rotationX
        frame.f_locals["rotationY"] = p.rotationY
        frame.f_locals["rotationZ"] = p.rotationZ
        frame.f_locals["pRotationX"] = p.pRotationX
        frame.f_locals["pRotationY"] = p.pRotationY
        frame.f_locals["pRotationZ"] = p.pRotationZ
        #frame.f_locals["turnAxis"] = p.turnAxis
        frame.f_locals["setMoveThreshold"] = p.setMoveThreshold
        frame.f_locals["setShakeThreshold"] = p.setShakeThreshold
        frame.f_locals["isKeyPressed"] = p.isKeyPressed
        frame.f_locals["keyIsPressed"] = p.keyIsPressed
        frame.f_locals["key"] = p.key
        frame.f_locals["keyCode"] = p.keyCode
        frame.f_locals["keyIsDown"] = p.keyIsDown
        frame.f_locals["mouseX"] = p.mouseX
        frame.f_locals["mouseY"] = p.mouseY
        frame.f_locals["winMouseX"] = p.winMouseX
        frame.f_locals["winMouseY"] = p.winMouseY
        frame.f_locals["mouseButton"] = p.mouseButton
        frame.f_locals["mouseIsPressed"] = p.mouseIsPressed
        frame.f_locals["touches"] = p.touches
        frame.f_locals["createImage"] = p.createImage
        frame.f_locals["saveCanvas"] = p.saveCanvas
        frame.f_locals["saveFrames"] = p.saveFrames
        frame.f_locals["loadImage"] = p.loadImage
        frame.f_locals["image"] = p.image
        frame.f_locals["tint"] = p.tint
        frame.f_locals["noTint"] = p.noTint
        frame.f_locals["imageMode"] = p.imageMode
        frame.f_locals["pixels"] = p.pixels
        frame.f_locals["blend"] = p.blend
        frame.f_locals["copy"] = p.copy
        frame.f_locals["filter"] = p.filter
        frame.f_locals["get"] = p.get
        frame.f_locals["loadPixels"] = p.loadPixels
        frame.f_locals["set"] = p.set
        frame.f_locals["updatePixels"] = p.updatePixels
        frame.f_locals["loadJSON"] = p.loadJSON
        frame.f_locals["loadStrings"] = p.loadStrings
        frame.f_locals["loadTable"] = p.loadTable
        frame.f_locals["loadXML"] = p.loadXML
        frame.f_locals["loadBytes"] = p.loadBytes
        frame.f_locals["httpGet"] = p.httpGet
        frame.f_locals["httpPost"] = p.httpPost
        frame.f_locals["httpDo"] = p.httpDo
        frame.f_locals["createWriter"] = p.createWriter
        frame.f_locals["save"] = p.save
        frame.f_locals["saveJSON"] = p.saveJSON
        frame.f_locals["saveJSONObject"] = p.saveJSONObject
        frame.f_locals["saveJSONArray"] = p.saveJSONArray
        frame.f_locals["saveStrings"] = p.saveStrings
        frame.f_locals["saveTable"] = p.saveTable
        frame.f_locals["writeFile"] = p.writeFile
        frame.f_locals["downloadFile"] = p.downloadFile
        #frame.f_locals["abs"] = p.abs
        frame.f_locals["ceil"] = p.ceil
        frame.f_locals["constrain"] = p.constrain
        frame.f_locals["dist"] = p.dist
        frame.f_locals["exp"] = p.exp
        frame.f_locals["floor"] = p.floor
        frame.f_locals["lerp"] = p.lerp
        frame.f_locals["log"] = p.log
        frame.f_locals["mag"] = p.mag
        frame.f_locals["map"] = p.map
        #frame.f_locals["max"] = p.max
        #frame.f_locals["min"] = p.min
        frame.f_locals["norm"] = p.norm
        frame.f_locals["pow"] = p.pow
        frame.f_locals["round"] = p.round
        frame.f_locals["sq"] = p.sq
        frame.f_locals["sqrt"] = p.sqrt
        frame.f_locals["createVector"] = p.createVector
        frame.f_locals["noise"] = p.noise
        frame.f_locals["noiseDetail"] = p.noiseDetail
        frame.f_locals["noiseSeed"] = p.noiseSeed
        frame.f_locals["randomSeed"] = p.randomSeed
        frame.f_locals["random"] = p.random
        frame.f_locals["randomGaussian"] = p.randomGaussian
        frame.f_locals["acos"] = p.acos
        frame.f_locals["asin"] = p.asin
        frame.f_locals["atan"] = p.atan
        frame.f_locals["atan2"] = p.atan2
        frame.f_locals["cos"] = p.cos
        frame.f_locals["sin"] = p.sin
        frame.f_locals["tan"] = p.tan
        frame.f_locals["degrees"] = p.degrees
        frame.f_locals["radians"] = p.radians
        frame.f_locals["angleMode"] = p.angleMode
        frame.f_locals["textAlign"] = p.textAlign
        frame.f_locals["textLeading"] = p.textLeading
        frame.f_locals["textSize"] = p.textSize
        frame.f_locals["textStyle"] = p.textStyle
        frame.f_locals["textWidth"] = p.textWidth
        frame.f_locals["textAscent"] = p.textAscent
        frame.f_locals["textDescent"] = p.textDescent
        frame.f_locals["loadFont"] = p.loadFont
        frame.f_locals["text"] = p.text
        frame.f_locals["textFont"] = p.textFont
        frame.f_locals["append"] = p.append
        frame.f_locals["arrayCopy"] = p.arrayCopy
        frame.f_locals["concat"] = p.concat
        frame.f_locals["reverse"] = p.reverse
        frame.f_locals["shorten"] = p.shorten
        frame.f_locals["shuffle"] = p.shuffle
        frame.f_locals["sort"] = p.sort
        frame.f_locals["splice"] = p.splice
        frame.f_locals["subset"] = p.subset
        frame.f_locals["float"] = p.float
        frame.f_locals["int"] = p.int
        frame.f_locals["str"] = p.str
        frame.f_locals["boolean"] = p.boolean
        frame.f_locals["byte"] = p.byte
        frame.f_locals["char"] = p.char
        frame.f_locals["unchar"] = p.unchar
        frame.f_locals["hex"] = p.hex
        frame.f_locals["unhex"] = p.unhex
        frame.f_locals["join"] = p.join
        frame.f_locals["match"] = p.match
        frame.f_locals["matchAll"] = p.matchAll
        frame.f_locals["nf"] = p.nf
        frame.f_locals["nfc"] = p.nfc
        frame.f_locals["nfp"] = p.nfp
        frame.f_locals["nfs"] = p.nfs
        frame.f_locals["split"] = p.split
        frame.f_locals["splitTokens"] = p.splitTokens
        frame.f_locals["trim"] = p.trim
        frame.f_locals["day"] = p.day
        frame.f_locals["hour"] = p.hour
        frame.f_locals["minute"] = p.minute
        frame.f_locals["millis"] = p.millis
        frame.f_locals["month"] = p.month
        frame.f_locals["second"] = p.second
        frame.f_locals["year"] = p.year
        frame.f_locals["plane"] = p.plane
        frame.f_locals["box"] = p.box
        frame.f_locals["sphere"] = p.sphere
        frame.f_locals["cylinder"] = p.cylinder
        frame.f_locals["cone"] = p.cone
        frame.f_locals["ellipsoid"] = p.ellipsoid
        frame.f_locals["torus"] = p.torus
        frame.f_locals["orbitControl"] = p.orbitControl
        frame.f_locals["debugMode"] = p.debugMode
        frame.f_locals["noDebugMode"] = p.noDebugMode
        frame.f_locals["ambientLight"] = p.ambientLight
        frame.f_locals["directionalLight"] = p.directionalLight
        frame.f_locals["pointLight"] = p.pointLight
        frame.f_locals["loadModel"] = p.loadModel
        frame.f_locals["model"] = p.model
        frame.f_locals["loadShader"] = p.loadShader
        frame.f_locals["createShader"] = p.createShader
        frame.f_locals["shader"] = p.shader
        frame.f_locals["normalMaterial"] = p.normalMaterial
        frame.f_locals["texture"] = p.texture
        frame.f_locals["ambientMaterial"] = p.ambientMaterial
        frame.f_locals["specularMaterial"] = p.specularMaterial

        def myCreateCanvas(*args):
            p.createCanvas(*args)
            frame.f_locals["width"] = p.width
            frame.f_locals["height"] = p.height

        frame.f_locals["createCanvas"] = myCreateCanvas

        def captureMouse():
            frame.f_locals["mouseX"] = p.mouseX
            frame.f_locals["mouseY"] = p.mouseY
            frame.f_locals["pmouseX"] = p.pmouseX
            frame.f_locals["pmouseY"] = p.pmouseY

            frame.f_locals["mouseIsPressed"] = p.mouseIsPressed
            frame.f_locals["mouseButton"] = p.mouseButton
            frame.f_locals["frameCount"] = p.frameCount
            frame.f_locals["width"] = p.width
            frame.f_locals["height"] = p.height

        def captureKeyboard():
            frame.f_locals["keyCode"] = p.keyCode
            frame.f_locals["key"] = p.key
            frame.f_locals["keyIsPressed"] = p.keyIsPressed


        def myMousePressed():
            captureMouse()
            if 'mousePressed' in frame.f_locals:
                frame.f_locals['mousePressed']()

        def myMouseReleased():
            captureMouse()
            if 'mouseReleased' in frame.f_locals:
                frame.f_locals['mouseReleased']()

        def myMouseClicked():
            captureMouse()
            if 'mouseClicked' in frame.f_locals:
                frame.f_locals['mouseClicked']()

        def myMouseMoved():
            captureMouse()
            if 'mouseMoved' in frame.f_locals:
                frame.f_locals['mouseMoved']()

        def myMouseDragged():
            captureMouse()
            if 'mouseDragged' in frame.f_locals:
                frame.f_locals['mouseDragged']()

        def myKeyPressed():
            captureKeyboard()
            if 'keyPressed' in frame.f_locals:
                frame.f_locals['keyPressed']()

        def myKeyReleased():
            captureKeyboard()
            if 'keyReleased' in frame.f_locals:
                frame.f_locals['keyReleased']()

        def myKeyTyped():
            captureKeyboard()
            if 'keyTyped' in frame.f_locals:
                frame.f_locals['keyTyped']()

        def mySetup():
            captureMouse()
            if 'setup' in frame.f_locals:
                frame.f_locals['setup']()

        def myPreload():
            captureMouse()
            if 'preload' in frame.f_locals:
                frame.f_locals['preload']()

        def myDraw():
            captureMouse()
            captureKeyboard()
            if 'draw' in frame.f_locals:
                frame.f_locals['draw']()


        p.setup = mySetup # setup
        p.draw = myDraw #draw
        p.mouseMoved = myMouseMoved
        p.mouseDragged = myMouseDragged
        p.mousePressed = myMousePressed
        p.mouseClicked = myMouseClicked
        p.mouseReleased = myMouseReleased
        p.preload = myPreload
        p.keyTyped = myKeyTyped
        p.keyPressed = myKeyPressed
        p.keyReleased = myKeyReleased

        
    myp5 = window.p5.new(sketch)