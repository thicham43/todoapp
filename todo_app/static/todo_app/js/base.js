console.log("hello");


function show_actions(row_nbr){
    hide_openDropdowns();
    show_dropdown_neighbors();
    const dropdown_neighbor = document.getElementById("actions_dropdown_neighbor-"+row_nbr);
    dropdown_neighbor.classList.toggle("hidden");
    const dropdown = document.getElementById("actions_dropdown-"+row_nbr);
    dropdown.classList.toggle("hidden");
}

window.onclick = function(event) {
                    if (!event.target.matches('#actions_dropdown_btn')) {
                        hide_openDropdowns();
                        show_dropdown_neighbors();
                    }
                }

function hide_openDropdowns(){
    const dropdowns = document.getElementsByClassName("dropdown-panel");
    for (var i = 0; i < dropdowns.length; i++) {
        const openDropdown = dropdowns[i];
        if (!openDropdown.classList.contains('hidden')) {
            openDropdown.classList.add('hidden');
        }
    }
}

function show_dropdown_neighbors(){
    const dropdown_neighbors = document.getElementsByClassName("dropdown-neighbor");
    for (var i = 0; i < dropdown_neighbors.length; i++) {
        const neighbor = dropdown_neighbors[i];
        if (neighbor.classList.contains('hidden')) {
            neighbor.classList.remove('hidden');
        }
    }
}
