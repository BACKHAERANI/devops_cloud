import '../components/TopNav.css'


function TopNav({changePageName}){
    return(
        <ul className='top-nav'>
            <li>
               <a onClick={() => changePageName("about")}>About</a>
            </li>
            <li>
               <a onClick={() => changePageName("counter")}> Counter</a>
            </li>
            <li>
                <a onClick={() => changePageName("Lotto")}>Lotto</a>
            </li>
            <li> 
                <a onClick={() => changePageName("Playlist")}>Play,Youtube</a>
            </li>
        </ul>
    );
}

export default TopNav;