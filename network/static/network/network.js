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
            post.style['background-color'] = 'red';
            post.querySelector('.post-text').style.color ='white';
            fetch(`/edit/${postpk}`, {
                method: "GET"
              })    
              .then(response => response.json())
              .then(result => {
                console.log(result);
                let textArea = document.createElement('textarea');
                textArea.innerHTML = result.text;
                post.append(textArea);
                });
        }
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