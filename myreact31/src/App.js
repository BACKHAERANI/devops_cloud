import PageLotto from "./PageLotto ";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import TopNav from "./TopNav";
import profilelist from "./Profile.json";

function App() {
  const [pageName, setPageName] = useState();
  const [profilePage, setProfilePage] = useState(profilelist[0].name);

  return (
    <div>
      <TopNav changePage={setPageName} />
      {pageName === "Lotto" && <PageLotto />}

      {pageName === "Profile" &&
        profilelist.map((list, index) => {
          if (profilePage === list.name) {
            return (
              <div className={`member${index % 4}`}>
                <ProfileCard
                  changePage={setProfilePage}
                  name={list.name}
                  role={list.role}
                  facebook_url={list.facebook_url}
                  email={list.email}
                  profileImage={list.image}
                >
                  <nav>
                    {profilelist.map((list) => {
                      return (
                        <a
                          className={profilePage === list.name ? "on" : "off"}
                          onClick={() => setProfilePage(list.name)}
                        ></a>
                      );
                    })}
                  </nav>
                </ProfileCard>
              </div>
            );
          }
        })}
    </div>
  );
}

export default App;
