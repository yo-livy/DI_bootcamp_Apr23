((childrenNum, namePartner, location, job)=> {
    const divNode = document.createElement('div');
    const textNode = document.createTextNode(`You will be a ${job} in ${location}, and married to ${namePartner} with ${childrenNum} kids.`);
    divNode.appendChild(textNode);
    document.body.appendChild(divNode);
})(4, 'Monica', 'LA', 'Software developer');
