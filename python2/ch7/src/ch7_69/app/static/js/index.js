(function(){
    "use strict";
    var g = {elm: {}};
    g.elm.txt_art_nam = document.getElementById("txt_art_nam");
    g.elm.txt_art_als = document.getElementById("txt_art_als");
    g.elm.txt_art_tag = document.getElementById("txt_art_tag");
    g.elm.btn_search = document.getElementById("btn_search");

    window.onload = function () {
        g.elm.txt_art_nam.value = "";
        g.elm.txt_art_als.value = "";
        g.elm.txt_art_tag.value = "";
        g.elm.btn_search.value = "";
    };

    g.elm.btn_search.onclick = function () {
        searchArtist();
    };

    // 検索APIを叩くだけ
    function searchArtist(){
        var api
          , parm
          , uri
          , json;
        api = "./search";
        parm = "name=" + g.elm.txt_art_nam.value + "&alias=" + g.elm.txt_art_als.value + "&tag=" + g.elm.txt_art_tag.value;
        uri = api + "?" + parm
        //location.href + api + "?" + parm;
        json = syncGetRequest(uri);
    }
})();
