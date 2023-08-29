
let searchForm = document.getElementById("searchForm")
let pageLinks = document.getElementsByClassName("page-link")

if (searchForm){
    for(let i=0; i < pageLinks.length; i++){
        pageLinks[i].addEventListener("click", function(e){

            // PREVENT THE DEFAULT ACTIONS WHEN CLICK THOSE BUTTONS
            e.preventDefault()
            
            // GET THE DATA ATTRIBUTE (from 'data-page' attribute in pagination.html)
            let page = this.dataset.page

            // ADD HIDDEN SEARCH INPUT TO FORM (TO PASS THE VALUE OF THE 'page' ALONG WITH 'search_query')
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`

            // SUBMIT THE FORM (search_quey & page)
            searchForm.submit()

        })
    }
}
