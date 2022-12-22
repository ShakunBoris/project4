document.addEventListener("DOMContentLoaded", function () {
    // only for profile page
  const follow = document.querySelector("#follow-button");
  if (follow) {follow.addEventListener("click", folUnfol)};
  // for all pages where edit
  const editButtons = document.querySelectorAll(".edit-button");
  if (editButtons) {editButtons.forEach(edit)};
});


function edit(btn) {
        btn.onclick = function() {
            // alert(this.dataset.postpk);
            console.log('this', this.dataset.postpk);
            console.log('btn', btn.dataset.postpk);
            let postpk = btn.dataset.postpk;
            let post = document.querySelector(`#post${postpk}`);
            post.style['background-color'] = 'grey';
            post.querySelector('.post-text').style.color ='white';
            fetch(`/edit/${postpk}`, {
                method: "GET"
              })    
              .then(response => response.json())
              .then(result => {
                console.log(result);
                // let textArea = document.createElement('textarea');
                // textArea.innerHTML = result.text;
                // post.querySelector('.post-text').replaceWith(textArea);
                // textArea.outerHTML = '<li>'+ textArea.outerHTML + '</li>';
                post.querySelector('.post-text').innerHTML = '<textarea>' + post.querySelector('.post-text').innerHTML.slice(10,) + '</textarea>'
                let save = document.createElement('button');
                save.innerHTML = 'save';
                save.dataset.postpk = postpk;
                save.onclick = saveFunc;
                post.querySelector('ul').append(save);
                });
        }
}


function saveFunc() {
    postpk = this.dataset.postpk;
    console.log(postpk);
    newText = document.querySelector(`#post${postpk} textArea`).value;
    console.log(newText);
    fetch(`/edit/${postpk}`, {
        method: 'PUT',
        body: JSON.stringify({
            postpk: postpk,
            text: newText
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result.status);})
}

function folUnfol() {
    // Fetch PUT to renew DB and button
    console.log(this.dataset.profile)
    console.log(typeof this.dataset.profile)
    fetch(`/user/${this.dataset.profile}`, {
        method: 'PUT',
        body: JSON.stringify({
            folUnfol: true,  
        })
    }).then(() => {
    if (document.querySelector('#follow-button').innerHTML.includes('Unfollow')) {
        console.log('REMOVING')
        document.querySelector('#follow-button').innerHTML = 'Follow'
    } else {
        console.log('ADDING')
        document.querySelector('#follow-button').innerHTML = 'Unfollow'
    }
    })
}