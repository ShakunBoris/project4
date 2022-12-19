document.addEventListener("DOMContentLoaded", function () {
  const follow = document.querySelector("#follow-button");
  if (follow) {follow.addEventListener("click", folUnfol)}
});

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