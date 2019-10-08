function syncGetRequest(uri) {
    "use strict";
    var req = new XMLHttpRequest();
    // 同期通信
    req.open("GET", uri, false);
    req.send();
    if (req.status === 200) {
        // リダイレクトの判定
        var redURI = req.getResponseHeader("AjaxRedirect");
        if (redURI) {
            window.location.href = redURI;
            return null;
        } else {
            if (req.responseText) {
                return JSON.parse(req.responseText);
            } else {
                return null;
            }
        }
    } else if (req.status === 500) {
        throw new Error("致命的なエラーが発生しました：" + req.status);
    } else {
        throw new Error("致命的なエラーが発生しました：" + req.status);
    }
}