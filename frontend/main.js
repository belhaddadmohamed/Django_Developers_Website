
// FUNCTION COPIED FROM DJANGO DOCUMENTATTION (CREATE A TOKEN FOR THE FORM) (https://docs.djangoproject.com/fr/4.2/howto/csrf/)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



// BUILD THE LIST OF PROJECTS 
buildProjects()
function buildProjects(){
    url = "http://127.0.0.1:8000/api/projects/"
    projectWrapper = document.getElementById("projects--wrapper")

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){

        console.log(data)
        projects = data

        for(project in projects){
            project = projects[project]

            let projectCard = `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.featured_image}" />
                    
                    <div>
                        <div class="card--header">
                            <h3>${project.title}</h3>
                            <strong class="vote--option" data-vote="up" data-project="${project.id}" >&#43;</strong>
                            <strong class="vote--option" data-vote="down" data-project="${project.id}"  >&#8722;</strong>
                        </div>
                        <i>${project.vote_ratio}% Positive feedback </i>
                        <p>${project.description.substring(0, 150)}</p>
                    </div>
                
                </div>
            `
            projectWrapper.innerHTML += projectCard
        }
    })
}



// CREATE A PROJECT (ADD EVENT LISTENER TO SUBMIT THE FORM)
form = document.getElementById("form")

form.addEventListener('submit', function(event){
    event.preventDefault()
    console.log("Button Submit Clicked")
    console.log(csrftoken)

    fetch("http://127.0.0.1:8000/api/create-project/", {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "owner": null,
            "title": document.getElementById("id_title").value,
            "description": document.getElementById("id_description").value,
            "demo_link": document.getElementById("id_demo_link").value,
            "source_link": document.getElementById("id_source_link").value,
        })
    })
    .then(function(resp){
        buildProjects()
        form.reset()
    })

})



