/**
 * Assignment 7
 */

/** Load the list of albums */
function listAlbums() {
    // TODO make an AJAX request to /albums
    // then populate the "albums_list" list with the results


// function loadDoc() {
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//     document.getElementById("demo").innerHTML = this.responseText;
//     }
//     };
//     xhttp.open("GET", "ajax_info.txt", true);
//     xhttp.send();
// }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            var result = JSON.parse(xhttp.responseText);
            var b = document.getElementById("albums_list");


            for (var x=0; x< result.length; x++) {
                var li = document.createElement("li");
                li.innerHTML = "<a href='#' onclick='showAlbum(" + result[x].album_id + ")'>" + result[x].artist + " - " + result[x].title + "</a>";
                b.appendChild(li);
            }
        }
    };

    xhttp.open("GET", "/albums", true);
    xhttp.send(null);
}



/** Show details of a given album */
function showAlbum(album_id) {
    // TODO make an AJAX request to /albuminfo with the selected album_id as parameter (i.e., /albuminfo?album_id=xxx),
    // then show the album cover in the "album_cover" div and display the tracks in a table inside the "album_songs" div
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var result = JSON.parse(xhttp.responseText);

            document.getElementById("album_cover").innerHTML = "<img src='/static/images/" + result.cover_img + "' />";
            var thtml = "<table>\n<tr>\n<th>No.</th>\n<th>Title</th>\n<th>Length</th>\n</tr>\n";


            // for(var x=0; x<response['data'].length; x++){
            //     fbhtml += '<div class="baby_img">';
            //     fbhtml += '<input type="checkbox" id="facebook_'+x+'" name="facebook[]" value="'+response['data'][x]['source']+'" class="styled" />';
            //     fbhtml += '<img src="'+response['data'][x]['source']+'" class="img-responsive" style="width:100px !important; height:100px !important;" />';
            //     fbhtml += '</div>';
            // }
            for (var x=0; x< result.tracks.length; x++) {
                thtml += "<tr>\n";
                thtml += "<td class='song_no'>" + (x+1) + "</td>\n";
                thtml += "<td class='song_title'>" + result.tracks[x].title + "</td>\n";
                thtml += "<td class='song_length'>" + result.tracks[x].length + "</td>\n";
                thtml += "</tr>\n";
            }
            thtml += "<tr>\n";
            thtml += "<td colspan='2'><strong>Total length:</strong></td>\n";
            thtml += "<td class='song_length'><strong>" + result.length + "</strong></td>\n";
            thtml += "</tr>\n";
            thtml += "</table>"
            document.getElementById("album_songs").innerHTML = thtml;
        }
    };
    xhttp.open("GET", "/albuminfo?album_id=" + album_id, true);
    xhttp.send(null);
}
