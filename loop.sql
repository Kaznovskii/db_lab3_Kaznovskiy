DO $$
  DECLARE
    org_id Organizations.organization_id%TYPE;
    org_name Organizations.organization_name%TYPE;
    
  BEGIN
    org_id := 'Or';
    org_name := 'Org';
    FOR counter IN 1..5
      LOOP
        INSERT INTO Organizations (organization_id, organization_name)
        VALUES (org_id ||  counter + 10, org_name || counter + 10);
      END LOOP;
  END;
$$

SELECT * FROM organizations