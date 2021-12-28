import PageLotto from "./PageLotto ";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import profileImage from "./components/member1.jpg";
import TopNav from "./TopNav";
import Profilelist from "./Profile.json";

function App() {
  const [pageName, setPageName] = useState();
  const [profilePage, setProfilePage] = useState("해란");
  return (
    <div>
      <TopNav changePage={setPageName} />
      {pageName === "Lotto" && <PageLotto />}

      {pageName === "Profile" &&
        Profilelist.map((list) => {
          if (profilePage === list.name) {
            return (
              <ProfileCard
                changePage={setProfilePage}
                name={list.name}
                role={list.role}
                facebook_url={list.facebook_url}
                email={list.email}
                profileImage={profileImage}
              />
            );
          }
        })}
    </div>
  );
}

export default App;
