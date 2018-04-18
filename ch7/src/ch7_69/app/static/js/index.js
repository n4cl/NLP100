(function(){
"use strict";
let g = {elm: {}};
g.elm.txt_art_nam = document.getElementById("txt_art_nam");
g.elm.txt_alt_nam = document.getElementById("txt_alt_nam");
g.elm.txt_art_tag = document.getElementById("txt_art_tag");
g.elm.btn_search = document.getElementById("btn_serach");

g.row_lst.btn_lst_edit.onclickEx = function (sender) {
    var row = g.tbl_lst.getRowIndex(sender.element.id);
    clearDataMas();
    disabledElement(false);
    getDataMas(g.tbl_lst.rowWrappers[row].lbl_lst_ord_cod.getValue(), 0, g.val['MNT_MOD']);

    masDialogVisible(true);

    if(g.row_mas.lbl_mas_mnt_mod_nam.getValue() === "緊急"){
        g.row_mas.txt_mas_dll_dte.readOnly = true;
        g.row_mas.sel_mas_jan_kbn.focus();
    }else if(g.row_mas.lbl_mas_mnt_mod_nam.getValue() === "通常"){
        g.row_mas.txt_mas_dll_dte.readOnly = false;
        g.row_mas.txt_mas_dll_dte.focus();
    }

};

})()
