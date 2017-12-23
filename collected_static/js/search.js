/**
 * Created by jianping on 16-11-17.
 */
function jsmeOnLoad() {

    jsmeApplet = new JSApplet.JSME("jsme", "360px", "360px", {
        "options": "oldlook,star,nocanonize"
    });
    document.JME = jsmeApplet;
}

var CompoundDivHtml = function (d) {
    var com = $("#compound-div");
    com.html("");
    com.html(d);
};

var structureSearch = function () {
    var smiles = jsmeApplet.smiles();
    // console.log(data);
    $('#smiles').val(smiles);
    var data = $('#structure-form').serialize();
    $.ajax(
        {
            'cache': true,
            'url': 'structure/',
            'data': data,
            'type': 'POST',
            'error': function (e) {
                console.log(typeof e);
                console.log(e);
                console.log(e.responseText)
            },
            'success': function (d) {
                CompoundDivHtml(d);
                // $("#compound-table").dataTable();
            }
        }
    )
};


var identifySearch = function () {
    var data = $("#identify_form").serialize();
    console.log(data);
    $.ajax(
        {
            'cache': true,
            'url': 'identify/',
            'data': data,
            'type': 'POST',
            'error': function (e) {
                console.log(typeof e);
                console.log(e);
                console.log(e.responseText)
            },
            'success': function (d) {
                $("#compound-div").html(d);
                // $("#compound-table").dataTable();
            }
        }
    )
};


var search = function () {
    if ($("#drawer").attr("class").indexOf('active') > 0) {
        structureSearch();
    }
    else if ($("#identify").attr("class").indexOf('active') > 0) {
        identifySearch();
    }
};

