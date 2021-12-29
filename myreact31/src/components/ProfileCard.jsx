import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";
import { faFacebook, faInstagram } from "@fortawesome/free-brands-svg-icons";

function ProfileCard({
  unique_id,
  mbti,
  instagram_url,
  profile_image_url,
  name,
  role,
  children,
}) {
  return (
    <div>
      <section>
        <nav className="menu">
          <a href="#">
            <FontAwesomeIcon icon={faBars} />
          </a>
          <a href="#">
            <FontAwesomeIcon icon={faStickyNote} />
          </a>
        </nav>
        <article className="profile">
          <img src={profile_image_url} />
          <h1>{name}</h1>
          <h2>{role}</h2>
          <h2>{mbti}</h2>
          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faInstagram} className="icon" />
            <span>
              <a href="#">{instagram_url}</a>{" "}
            </span>
          </li>
          {/* <li>
            <FontAwesomeIcon icon={faEnvelope} />
            <span>{email}</span>
          </li> */}
        </ul>
        <nav className="others">{children}</nav>
      </section>
    </div>
  );
}
export default ProfileCard;
