# Assignment 5 - Vuejs

The task is to implement a classic memory game using Vuejs.

  -	The board is n-by-n, where n is your choosing (minimum 4).
  -	The deck contains unique pairs of cards (for a board of `n*n`, we need `n*n/2` pairs of cards). You can select the "theme" (e.g., places, cars, logos, etc.).
  - Rules of the game:
    *	Cards are laid out in a grid face down.
    * Two players take turns.
    * Player flips a pair of cards over. If the cards match, they stay flipped over (or disappear), the player scores one point, and gets a bonus turn.
    *	The game is over when all matches are found.
  - Card grid should be randomized for each game.
  -	Use some animation or effect for flipping the cards. 
    Check out [CSS transition](https://www.w3schools.com/css/css3_transitions.asp), [CSS 2D transform](https://www.w3schools.com/css/css3_2dtransforms.asp),
    [CSS 3D transform](https://www.w3schools.com/css/css3_3dtransforms.asp) and the example below.
  - Count and show on the screen the total time elapsed, the total number of flips and each players score
  - Show in the end which player won.
  - Allow to start a new game after finishing, without refreshing the page.
  - Use Vue.js: All, or most of the application should live inside a vue.js application. A good indicator that you do things right is, if you do not use `document` in your javascript.

The `samples/` folder in your GitHub repository contains some example screenshots. Note that the appearance is left to you, it doesn’t have to look the same. 

Commit and push the files to GitHub.

You may or may not find this example helpfull:
[Vuejs card component](https://github.com/dat310-spring21/course-info/tree/master/examples/js/vue2/card)


# Øving 5 - Vuejs

Oppgaven er å implementere et klassisk memory-spill ved hjelp av Vuejs.

  -	Brettet er `n*n`, der du velger n (minimum 4).
  -	Brettet inneholder unike par med kort (på et brett som er `n*n` trenger vi `n*n/2` kortpar). Du kan velge _theme_ (type bilder på kortene, f.eks. steder, biler, logoer etc.).
  - Spillereglene:
    *	Kortene legges ut i et rutenett med bildet ned.
    * To spillere snur kort annenhver gang.
    * Spilleren snur to kort om gangen. Hvis kortene er like, forblir de snudd (eller forsvinner), spilleren får et poeng og får snu en gang til.
    * Spillet er over når alle parene er funnet.
  - Posisjoner i rutenettet skal være nytt og tilfeldig for hvert spill.
  -	Bruk animasjon eller en effekt for å snu kortene. Sjekk [CSS transition](https://www.w3schools.com/css/css3_transitions.asp), [CSS 2D transform](https://www.w3schools.com/css/css3_2dtransforms.asp),
    [CSS 3D transform](https://www.w3schools.com/css/css3_3dtransforms.asp) og eksemplet under.
  - Tell og vis hvor lang tid som er gått og totalt antall kortpar som har blitt snudd.
  - Vis score for hvert spiller.
  - Vis i slutten hvilken spiller vant.
  - Det skal være mulig å starte spillet om igjen etter det er ferdig. Dette skal funke uten å laste inn siden på nytt.
  - Du skal bruke vuejs, så prøv å ikke bruke noen `document.` i JS koden.

I mappen `samples/` ligger noen skjermbilder med eksempler. Merk at du bestemmer selv hvordan applikasjonen ser ut, den må ikke nødvendigvis se ut som i eksemplene.

Commit og push filene til GitHub.

Kanskje denne er nyttige:
[Vuejs card component](https://github.com/dat310-spring21/course-info/tree/master/examples/js/vue2/card)
