import PageLotto from "./PageLotto ";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import TopNav from "./TopNav";
import profilelist from "./Profile.json";
import Axios from "axios";

function App() {
  const [pageName, setPageName] = useState();
  const [profilePage, setProfilePage] = useState(profilelist[0].name);

  // useEffect(() => {
  //   Axios.get(
  //     "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
  //   )
  //     .then((reponse) => {
  //       // reponse는 axios 객체
  //       // response.data => 응답 내용
  //       setProfileList(response.data);
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });
  // }, []);

  return (
    <div>
      <TopNav changePage={setPageName} />
      {pageName === "Lotto" && <PageLotto />}

      {pageName === "Profile" &&
        profilelist.map((profile, index) => {
          if (profilePage === profile.name) {
            return (
              <div className={`member${index % 4}`}>
                <ProfileCard changePage={setProfilePage} {...profile}>
                  <nav>
                    {profilelist.map((profile) => {
                      return (
                        <a
                          className={profilePage === profile.name ? "on" : ""}
                          onClick={() => setProfilePage(profile.name)}
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
