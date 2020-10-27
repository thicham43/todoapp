console.log("hello");

function display_mark_done(row_number){
    const row = document.getElementById("table-row-"+row_number);
    row.lastElementChild.firstElementChild.classList.remove("hidden");
}

function hide_mark_done(row_number){
    const row = document.getElementById("table-row-"+row_number);
    row.lastElementChild.firstElementChild.classList.add("hidden");
}