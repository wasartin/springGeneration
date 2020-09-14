
/**
 * An entity (or dao) that maps to the table 'account' in the Database. This represents the model of the object.
 * accounts can either be general accounts (allowed some functions and abilities), regisitered accounts (more functions) or admin
 * (they can do whatever).
 * @author watis
 *
 */
@Entity
@Table(name="account")
public class Account {

	/**
	 * account emails are used as ID's since they are unique
	 */
	@Id //specifies that this is a primary key
	@Column(name="account_email")
	private String account_email;//These names should exactly match the names of the db columns

	public account() {//No arg constructor required by JPA for building properly
		super();
	}
	
	public account(String account_email, String account_type) {
		super();
		this.account_email = account_email;
		this.account_type = account_type;
	}

	/**
	 * account type determines the abilities of the account
	 */
	@Column(name="account_type")
	private String account_type;

	public String getAccount_email() {
		return account_email;
	}
	public void setAccount_email(String account_email) {
		this.account_email = account_email;
	}
	public String getAccount_type() {
		return account_type;
	}
	public void setAccount_type(String account_type) {
		this.account_type = account_type;
	}
}
