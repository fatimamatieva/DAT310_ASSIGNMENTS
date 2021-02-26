var e;
let samlet = [];
let valg;
window.addEventListener("keypress", ev => {
    if (ev.keyCode === 32) {
        spill();
    }
})
function arrayShuffle(array) {
    let newPos;
    for (let i = array.length - 1; i > 0; i--) {
        const newPos = Math.floor(Math.random() * (i + 1));
        [array[i], array[newPos]] = [array[newPos], array[i]];
    }
    return
}
function spill() {
    let Flippet = 0;
    let board = document.querySelector("#cardboard");
    const del = ['a.gif', 'b.gif', 'c.gif', 'd.gif', 'e.gif', 'f.gif', 'g.gif', 'h.gif']
    //dele array:
    let samlinglist = [...del, ...del]; 
    //returns the HTML content of an element
    board.innerHTML = "";
    arrayShuffle(samlinglist);
    var score = new Vue({
        el: "#antallflips",
        data: {
            Flippet: 0
        }
    });
    for (let i = 0; i < 16; i++) {
        let card = document.createElement("div");
        var new_cards = new Vue({
            template: `
            <div class="cardboard">
                <div class="outer" v-on:click="flip">
                    <div class="card front" v-bind:style="{ transform:flipped ? 'rotateZ(1080deg)': 'none', display: removed ? 'none': ''}">
                        <img :src="samling">
                    </div>
                    <div class="card back" v-bind:style="{ transform : flipped? 'rotateY(-180deg)': 'none', display : removed ? 'none':''}"></div>
                </div>
            </div>
            `,
            data: function() {
                return {
                    id: i,
                    samling: samlinglist[i],
                    flipped: false,
                    matched: false,
                    removed: false
                };
            },
            methods: {
                flip: function(o) {
                    if (valg === undefined) {
                        this.flipped = true;
                        valg = this;
                    } else {
                        if (valg.id == this.id) { 
                            // true, ikke flippe tilbake det valgte kortet
                            this.flipped = true;
                        } else {
                            this.flipped = true;
                            if (valg.samling === this.samling) { // Hvis bruker gjetter riktig, fjern kort med SetTimeout
                                if (spiller1.turn) {
                                    spiller1.count1++;
                                } else if (spiller2.turn) {
                                    spiller2.count2++;
                                }
                                score.Flippet++;
                                samlet.push(valg.samling); //legger til listen min slikt at jeg kan se når spillet er ferdig 
                                setTimeout((x) => {
                                    x.removed = true;
                                    this.removed = true;
                                }, 500, valg);
                                vunnet();
                            } else { // Hvis bruker gjetter feil, snu kortet
                                setTimeout((x) => {
                                    x.flipped = false;
                                    this.flipped = false;
                                }, 800, valg);
                                score.Flippet++;
                                if (spiller1.turn) {
                                    spiller1.turn = false;
                                    spiller2.turn = true;
                                } else if (spiller2.turn) {
                                    spiller1.turn = true;
                                    spiller2.turn = false;
                                }
                            }
                        }
                        valg = undefined; // reset choiceA
                        console.log("Amount of flips during this game: " + Flippet);
                    }
                    this.function(o.target)
                },
            }
        });
        board.appendChild(card);
        new_cards.$mount(card);
    }
    board.style.width = 115 * 4 + 'px';
}
function vunnet() {
    if (samlet.length == 8) {
        if (spiller2.count2 > spiller1.count1) {
            alert("SPILLER2 VANT")
        } else {
            alert("SPILLER1 VANT")
        }
    }
};