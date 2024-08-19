# Framework-Braille-Display
A braille display for the Framework 13 laptop's touchpad, hopefully

## Project Status

⚠️ This project is still a work in progress. It is not usable, yet. ⚠️

If you are interested in helping design, test, or advise on this project, please reach out!

I'm not sure how long this project will take. The goal is to have a proof of concept by 2025-06-01.

## What is this?

This is a project to create a refreshable braille display, which is installable in the location of the Framework 13 laptop's touchpad.

A braille display is a device that allows blind and visually impaired people to read text on a computer screen by converting it to braille.

Manufacturing techniques, cost, etc. TBD.

## Why?

I am not blind. I am, however, disappointed in the lack of laptop-compatible braille displays, and the lack of affordable braille displays in general. I believe that an addition to the open source Framework laptop is a great way to make computers more accessible to visually impaired people from all countries.

## Resources and Inspiration

This project starts by building on the work of others.

### Very Good Reference: Vijay's Braille Display

* Links:
    * https://hackaday.io/project/10849-refreshable-braille-display
    * https://hackaday.io/project/191181-electromechanical-refreshable-braille-module
    * MIT Project: https://web.archive.org/web/20230322053540/https://www.angadmakes.com/my-portfolio/virtual-brailler
    * https://www.youtube.com/watch?v=BXi1tG78AW4

* Expansion ideas:
    * SMT inductor coils
        * **Core Type** filter: Drum Core; Drum Core, Wirewound; Powdered Iron Core
        * **Core Material** filter: NOT Alumina; Ceramic; Non-Magnetic
    * In-PCB flexure actuators (from video below)

### Potential References, BOM Sources, etc.
* Ultra-Thin Flexure Actuators with Printed Circuits:
    * https://www.youtube.com/watch?v=wrnBW0HD0Vo
    * https://microbots.io/
* https://www.solarbotics.com/?s=pager+motor&post_type=product&dgwt_wcas=1
* https://www.guysmagnets.com/neodymium-magnets-c11/guys-magnets-1-mm-x-0-5-mm-n52-high-grade-neodymium-disk-100-piece-pack-p27009
* Pogo Pins from Aliexpress/Digikey/LCSC

### Work-in-Progress/Inspiration-Only References
* 3D Printed Braille Display (unknown quality/completion): https://www.thingiverse.com/thing:90144
* DIY Braille Display and input device: https://github.com/brailletouch/Brailletouch
* DISBRA Research Paper:
    * An Enhanced Open Source Refreshable Braille Display DISBRA 2.0
    * DOI: `10.1007/978-3-030-78092-0_27`, Pages 423-435
    * Do _not_ use Sci-Hub to access this paper.
    * Uses two rotating octagonal drums with Braille line combination.
* MOLBED (Modular Low Cost Braille Electronic Display):
    * https://www.instructables.com/MOLBED-Modular-Low-Cost-Braille-Electronic-Display/
    * https://www.hackster.io/news/modular-low-cost-braille-electronic-display-molbed-f3872d53f0d3
    * Pin Assembly: https://www.youtube.com/watch?v=eobXfH6CkRc
* Software: https://libbraille.org/libbraille-a-software-to-easily-develop-braille-display/

### Community
* Braille Embosser (Printer): https://www.braillerap.org/en/

### Framework Laptop
* CAD and electrical specs for the Framework 13 laptop: https://github.com/FrameworkComputer/Framework-Laptop-13
