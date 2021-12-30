import { useState, useEffect } from "react";
import Axios from "axios";

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const handleRefresh = () => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h2>PageProfile</h2>
      <button onClick={() => setProfileList([])}>clear</button>
      <button onClick={handleRefresh}>새로고침</button>

      {profileList.length == 0 && <h3>등록된 프로필이 없습니다.</h3>}

      {profileList.map((member) => {
        return (
          <>
            <h3>
              [{member.unique_id}]{member.name}
            </h3>
            <ul>
              <img src={member.profile_image_url} />
              <li>{member.role}</li>
              <li>{member.instagram_url}</li>
              <li>{member.mbti}</li>
            </ul>
          </>
        );
      })}
    </div>
  );
}

export default PageProfile;
