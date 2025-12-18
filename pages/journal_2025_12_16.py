
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Debugging: Learning things the hard way", [])

@app.cell(hide_code=True)
def _():
    mo.md(r"""
# Debugging: Learning things the hard way

Writing code for a wide variety of project is a great way to learn new things and getting smarter. But sometimes, it's a painful and inefficient process. Let me introduce you to: the debugging hell.

Of course, some bugs are caused by you not having a big enough brain to see that your code is not correct for this particular case. But very often, the issue is that you don't know enough about the environment *around* your program. This includes libraries, weird decisions in standards, or how your OS works.

I learned some things this way. As I said, it's not efficient, and moreover it will probably never be useful to you. But anyway, here is a rant of random stuff I learned this way.
    - hashing in python is not deterministic. A salt is added before each execution, so when you try to setup a persistent cache is does not work.
    - iframes need a closing tag, even if nobody puts stuff inside. If you do `<iframe src="x.pdf"/>`, everything after the iframe will be invisible on your page. You need `<iframe src="x.pdf"></iframe>`
    - Monkey-C, the programming language created by Garmin that is *smartwatch-oriented* (they're geniuses), is weird. They have a concept called a *Symbol*. It's a compile-time construct, like a named constant pointer you can use instead of an enum. But when you create a menu, the identifiers of the choices are automatically converted to these *Symbols*. And funnily enough, you can't store *Symbols* in the device storage. So if you do a menu, get the choice of the user, store it in the long-term memory of the file, and try to retrieve it, you will get a crash without any error message. I you want the text associated with the menu option the user just clicked, have to do something like that:
        - <code><pre>
          var categoryStrings = {
            :work => Rez.Strings.CategoryWork,
            :friends => Rez.Strings.CategoryFriends,
            :family => Rez.Strings.CategoryFamily,
            :domestic => Rez.Strings.CategoryDomestic,
            :administrative => Rez.Strings.CategoryAdministrative,
            :hobbies => Rez.Strings.CategoryHobbies,
            :transport => Rez.Strings.CategoryTransport,
          };
          </pre></code>
        - And of course, one day I changed the definition of the menu and I forgot to change this mapping. It compiled fine, and then **the app crashed again, on my wrist !**
    - Some UTF-8 characters are not associated with a specified representation. They are called [Private user area characters](https://en.wikipedia.org/wiki/Private_Use_Areas). When you type one of these special symbols, what you see depends on your font. Try to paste this into other apps: ``, `` and my favourite: ` `
    - in [Systemd](https://github.com/blue-build/modules/issues/485), if you don't enable the `graphical.target`, your graphical environment won't start.
    - When you have "automatic reload libraries" enabled in Marimo, and you update a library, it will be indeed reloaded. So it will also update the cells that use this library. The thing is that if you used `marimo.dropdown` to select an item interactively, it will be reset to it's default value. AND WHAT HAPPENS IF YOU WERE ANALYSING A COMPLEX DATASET IN VECTOR SPACE AND THAT THE DEFAULT VALUE OF THE DROPDOWN IS A DUMMY DATASET THAT DOES NOT BEHAVE LIKE THE OTHERS ? Well, you try to find the error for a looong time.
    - If you want to disable part of your smartphone screen, you need to use [ADB](https://en.wikipedia.org/wiki/Android_Debug_Bridge) with this command: `adb shell wm overscan`. But to do it on modern devices, you need a root access. To do this you need to unroot your phone. Do do it you need to access your bootloader. And it turns out like some manufacturers like OPPO Neo 5 make it almost impossible to unroot your device. The only tool on the web with a potential way to do it was [a windows bash script written in chineese referenced on a WPS office document linked on a Reddit post](https://us.docs.wps.com/module/common/preview/?sid=sIIS95rToAcW2x7AG). And it can brick your device if you're not lucky.
    - Fedora uses [Selinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux), a linux kernel security module. And this module creates bug with a lot of software. I mean a lot. Just look at [the number of github issues related to it](https://en.wikipedia.org/wiki/Security-Enhanced_Linux), it's huge. For example, I encountered it while trying to install [the nix package manager](https://rottencandy.github.io/blog/fedora-nix/)
    - On Linux, all your wifi connections are stored in `/etc/NetworkManager/system-connections`. But if you try to archive them somewhere to reuse them on another computer, you will realize that it does not contain passwords, just the rest of the config.
    - In javascript, if you define a script in: `<head><script> ... </script></head>`, it will run when the page loads. But if you try to get an element with `getElementById`, it will fail. Indeed, the script is executed before the entire HTML tree is loaded. You need to add the [defer](https://developer.mozilla.org/en-US/docs/Web/API/HTMLScriptElement/defer) attribute to make sure it is executed after the HTML loads.
    - I am obsessed with github issues. When I try a new #OpenSource library, and I notice something strange, I immediately reproduce it, create a Minimal Reproducible Example, and fill an issue. And very often, my issue ends with "It took hours before I realize the issue came from your library".
        - (Just bragging, here is the list of the > 200 issues I opened: https://github.com/search?q=is%3Aissue%20author%3Arambip&type=issues)
        - [In the bokeh ploting library](https://github.com/bokeh/bokeh/issues/14657), the smart ticking is probably too smart
        - In the same library, if you want to know what the available symbols for plotting are (`Marker` types in bokeh's terminology), you go to the documentation of the "Marker" class right ? Wrong, you have to go to "Scatter". And [there is no link from Marker to Scatter](in [Systemd](https://github.com/blue-build/modules/issues/485), if you don't enable the `graphical.target`, your graphical environment won't start.)
    - (this list will probably keep growing, unless 1°: I die or 2°: I am so sick about computers I decide to become a cook instead.)
    - ![](https://imgs.xkcd.com/comics/actual_progress_2x.png)
        - credits: [xkcd](https://xkcd.com/2797/)
""")
